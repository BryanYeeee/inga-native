from uuid import uuid4

import boto3
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_url(request):
	content_type = request.data.get("content_type")

	if not content_type:
		return Response(
			{"detail": "content_type is required."},
			status=status.HTTP_400_BAD_REQUEST,
		)

	if not isinstance(content_type, str) or len(content_type) > 255:
		return Response(
			{"detail": "content_type must be valid."},
			status=status.HTTP_400_BAD_REQUEST,
		)

	key = f"photos/{uuid4()}"
	s3 = boto3.client(
		"s3",
		endpoint_url=settings.R2_ENDPOINT_URL,
		aws_access_key_id=settings.R2_ACCESS_KEY_ID,
		aws_secret_access_key=settings.R2_SECRET_ACCESS_KEY,
		region_name="auto",
	)
	upload_url = s3.generate_presigned_url(
		"put_object",
		Params={
			"Bucket": settings.R2_BUCKET_NAME,
			"Key": key,
			"ContentType": content_type,
		},
		ExpiresIn=900,  # 900 seconds = 15 minutes TODO: make a defined constant
	)

	return Response({"key": key, "upload_url": upload_url})

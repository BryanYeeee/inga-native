import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def authenticated_client(client, db):
	user = get_user_model().objects.create_user(
		username="pytest-user",
		password="pytest-password",
	)
	client.force_login(user)
	return client, user

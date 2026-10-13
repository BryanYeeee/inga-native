import pytest
from django.contrib.auth import get_user_model


def test_project_uses_its_own_user_model():
    """Fails if anything points the project back at Django's auth.User."""
    assert get_user_model()._meta.label == "accounts.User"


@pytest.mark.django_db
def test_can_create_a_field_worker():
    user = get_user_model().objects.create_user(
        username="fieldworker",
        password="not-a-real-password",
    )

    assert user.pk is not None
    assert user.check_password("not-a-real-password")

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """An Inga field worker or admin.

    Empty for now. AbstractUser already covers username, password, first and
    last name, email and the is_staff / is_active flags. It exists so that
    AUTH_USER_MODEL points at our own table from the first migration.
    """

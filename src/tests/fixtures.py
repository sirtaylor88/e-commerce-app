import pytest


@pytest.fixture
def create_admin_user(django_user_model):
    """Return an admin user"""
    return django_user_model.objects.create_superuser(
        "admin", "test@gmail.com", "qwerty"
    )

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command


@pytest.fixture(scope="session")
def custom_django_db_setup(django_db_setup, django_db_blocker):
    """Load db"""
    # https://pytest-django.readthedocs.io/en/latest/database.html#django-db-setup
    # https://pytest-django.readthedocs.io/en/latest/database.html#django-db-blocker
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")

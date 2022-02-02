import pytest
from src.inventory.models import Category


@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(
    db, custom_django_db_setup, id, name, slug, is_active
):
    result = Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("fashion", "fashion", 1),
        ("trainers", "trainers", 1),
        ("baseball", "baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(
    db, category_factory, name, slug, is_active
):
    result = category_factory.create(
        name=name,
        slug=slug,
        is_active=is_active,
    )
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active

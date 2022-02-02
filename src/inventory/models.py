from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Inventory Category table implemented with MPTT
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        max_length=120,
        blank=False,
        null=False,
        hepl_text=_("Required, 120 characters max."),
    )

    slug = models.SlugField(
        verbose_name=_("Category Safe URL"),
        max_length=150,
        blank=False,
        null=False,
        hepl_text=_("Only alphanumeric, underscores, hyphens allowed"),
    )

    is_active = models.BooleanField(default=True)

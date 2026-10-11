from django.db import models
from django.db.models.fields.related_descriptors import RelatedManager as RelatedDescriptorsRelatedManager
from django.db.models.manager import RelatedManager
from typing_extensions import assert_type


class Book(models.Model): ...


def check_related_manager_reexport(manager: RelatedDescriptorsRelatedManager[Book]) -> None:
    assert_type(manager, RelatedManager[Book])

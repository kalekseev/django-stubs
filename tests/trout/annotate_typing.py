from __future__ import annotations

# mypy: disable-error-code="assert-type,attr-defined"
from typing import TYPE_CHECKING, Protocol

from django.db import models
from typing_extensions import assert_type

if TYPE_CHECKING:
    from ty_extensions import Intersection


class HasDisplayName(Protocol):
    display_name: str


class AnnotatedModel(models.Model):
    name = models.CharField(max_length=100)

    def model_name(self) -> str:
        return self.name


class AnnotatedQuerySet(models.QuerySet[AnnotatedModel]):
    def custom_method(self) -> int:
        return 1

    def with_display_name(
        self,
    ) -> models.QuerySet[AnnotatedModel, Intersection[AnnotatedModel, HasDisplayName]]:
        return self.annotate(display_name=models.Value("display name"))


def check_annotated_row(queryset: AnnotatedQuerySet) -> None:
    assert_type(
        queryset.annotate(display_name=models.Value("display name")).custom_method(), int
    )
    annotated = queryset.with_display_name().get()
    assert_type(annotated.model_name(), str)
    assert_type(annotated.display_name, str)  # pyright: ignore[reportUnknownMemberType, reportAssertTypeFailure, reportAttributeAccessIssue]

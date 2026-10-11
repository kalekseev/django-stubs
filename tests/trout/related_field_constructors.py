from typing import Any
from typing_extensions import assert_type
from django.db import models
from django.db.models.fields.related import ForeignObject


class Organization(models.Model): ...


class Holder(models.Model):
    fk_class = models.ForeignKey(to=Organization, on_delete=models.CASCADE)
    fk_class_null = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    fk_string = models.ForeignKey("app.Organization", on_delete=models.CASCADE)
    fk_string_null = models.ForeignKey("app.Organization", on_delete=models.CASCADE, null=True)
    fk_typed = models.ForeignKey[Organization]("app.Organization", on_delete=models.CASCADE)
    fk_typed_null = models.ForeignKey[Organization | None]("app.Organization", on_delete=models.CASCADE, null=True)
    one_class = models.OneToOneField(Organization, on_delete=models.CASCADE)
    one_class_null = models.OneToOneField(Organization, on_delete=models.CASCADE, null=True)
    one_string = models.OneToOneField("app.Organization", on_delete=models.CASCADE)
    one_string_null = models.OneToOneField("app.Organization", on_delete=models.CASCADE, null=True)
    one_typed = models.OneToOneField[Organization]("app.Organization", on_delete=models.CASCADE)
    one_typed_null = models.OneToOneField[Organization | None]("app.Organization", on_delete=models.CASCADE, null=True)
    foreign_class = ForeignObject(Organization, on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"])
    foreign_class_null = ForeignObject(
        Organization, on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"], null=True
    )
    foreign_string = ForeignObject(
        "app.Organization", on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"]
    )
    foreign_string_null = ForeignObject(
        "app.Organization", on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"], null=True
    )
    foreign_typed = ForeignObject[Organization](
        "app.Organization", on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"]
    )
    foreign_typed_null = ForeignObject[Organization | None](
        "app.Organization", on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"], null=True
    )


def check(h: Holder) -> None:
    assert_type(h.fk_class, Organization)
    assert_type(h.fk_class_null, Organization | None)
    assert_type(h.fk_string, Any)
    assert_type(h.fk_string_null, Any | None)
    assert_type(h.fk_typed, Organization)
    assert_type(h.fk_typed_null, Organization | None)
    fk_class = models.ForeignKey(Organization, on_delete=models.CASCADE)
    assert_type(fk_class, models.ForeignKey[Organization])
    fk_class_null = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    assert_type(fk_class_null, models.ForeignKey[Organization | None])
    fk_string = models.ForeignKey("app.Organization", on_delete=models.CASCADE)
    assert_type(fk_string, models.ForeignKey[Any])
    fk_string_null = models.ForeignKey("app.Organization", on_delete=models.CASCADE, null=True)
    assert_type(fk_string_null, models.ForeignKey[Any | None])
    fk_typed = models.ForeignKey[Organization]("app.Organization", on_delete=models.CASCADE)
    assert_type(fk_typed, models.ForeignKey[Organization])
    fk_typed_null = models.ForeignKey[Organization | None]("app.Organization", on_delete=models.CASCADE, null=True)
    assert_type(fk_typed_null, models.ForeignKey[Organization | None])
    assert_type(h.one_class, Organization)
    assert_type(h.one_class_null, Organization | None)
    assert_type(h.one_string, Any)
    assert_type(h.one_string_null, Any | None)
    assert_type(h.one_typed, Organization)
    assert_type(h.one_typed_null, Organization | None)
    one_class = models.OneToOneField(Organization, on_delete=models.CASCADE)
    assert_type(one_class, models.OneToOneField[Organization])
    one_class_null = models.OneToOneField(Organization, on_delete=models.CASCADE, null=True)
    assert_type(one_class_null, models.OneToOneField[Organization | None])
    one_string = models.OneToOneField("app.Organization", on_delete=models.CASCADE)
    assert_type(one_string, models.OneToOneField[Any])
    one_string_null = models.OneToOneField("app.Organization", on_delete=models.CASCADE, null=True)
    assert_type(one_string_null, models.OneToOneField[Any | None])
    one_typed = models.OneToOneField[Organization]("app.Organization", on_delete=models.CASCADE)
    assert_type(one_typed, models.OneToOneField[Organization])
    one_typed_null = models.OneToOneField[Organization | None]("app.Organization", on_delete=models.CASCADE, null=True)
    assert_type(one_typed_null, models.OneToOneField[Organization | None])
    assert_type(h.foreign_class, Organization)
    assert_type(h.foreign_class_null, Organization | None)
    assert_type(h.foreign_string, Any)
    assert_type(h.foreign_string_null, Any | None)
    assert_type(h.foreign_typed, Organization)
    assert_type(h.foreign_typed_null, Organization | None)
    foreign_class = ForeignObject(Organization, on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"])
    assert_type(foreign_class, ForeignObject[Organization])
    foreign_class_null = ForeignObject(
        Organization, on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"], null=True
    )
    assert_type(foreign_class_null, ForeignObject[Organization | None])
    foreign_string = ForeignObject(
        "app.Organization", on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"]
    )
    assert_type(foreign_string, ForeignObject[Any])
    foreign_string_null = ForeignObject(
        "app.Organization", on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"], null=True
    )
    assert_type(foreign_string_null, ForeignObject[Any | None])
    foreign_typed = ForeignObject[Organization](
        "app.Organization", on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"]
    )
    assert_type(foreign_typed, ForeignObject[Organization])
    foreign_typed_null = ForeignObject[Organization | None](
        "app.Organization", on_delete=models.CASCADE, from_fields=["org_id"], to_fields=["id"], null=True
    )
    assert_type(foreign_typed_null, ForeignObject[Organization | None])


class CustomField(models.Field[str, str]):
    def __init__(self, label: str, **kwargs: Any) -> None:
        super().__init__(verbose_name=label, **kwargs)

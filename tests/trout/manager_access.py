from typing import Any, ClassVar

from django.contrib.auth.models import AnonymousUser, Group
from django.db import models
from django.db.models.manager import BaseManager, EmptyManager, ManagerDescriptor, ManyToManyRelatedManager, RelatedManager
from typing_extensions import assert_type


class BookQuerySet(models.QuerySet["Book"]):
    def published(self) -> "BookQuerySet":
        return self.filter(published=True)


class Book(models.Model):
    objects: ClassVar[models.Manager["Book", BookQuerySet]] = BookQuerySet.as_manager()
    alternate = models.Manager["Book"]()


class Through(models.Model): ...


class Author(models.Model):
    book_set: RelatedManager[Book, BookQuerySet]
    books: ManyToManyRelatedManager[Book, Through, BookQuerySet]


class Plain(models.Model): ...


class EmptyHolder:
    empty = EmptyManager(Book)


class DescriptorOwner(models.Model):
    custom = ManagerDescriptor(models.Manager["DescriptorOwner"]())


def valid_access(author: Author, anonymous: AnonymousUser, holder: EmptyHolder) -> None:
    assert_type(Book.objects, models.Manager[Book, BookQuerySet])
    assert_type(Book.objects.all(), BookQuerySet)
    assert_type(Book.alternate.get(), Book)
    assert_type(Plain.objects.get(), Plain)
    assert_type(DescriptorOwner.custom, BaseManager[Any])
    assert_type(author.book_set.all(), BookQuerySet)
    assert_type(author.books.all(), BookQuerySet)
    assert_type(holder.empty.all(), models.QuerySet[Book])
    assert_type(anonymous.groups.all(), models.QuerySet[Group])
    assert_type(Book._meta.default_manager.get(), Book)
    Book._meta.base_manager.all()


def forbidden_access(book: Book) -> None:
    book.objects  # type: ignore[arg-type]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[invalid-attribute-access]
    book.alternate  # type: ignore[arg-type]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[invalid-attribute-access]

from typing import TypeVar

from typing_extensions import assert_type

from django.db import models


class BookQuerySet(models.QuerySet["Book"]):
    def published(self) -> "BookQuerySet":
        return self.filter(published=True)


class BookManager(models.Manager["Book", BookQuerySet]):
    _queryset_class = BookQuerySet


class Book(models.Model):
    published = models.BooleanField()

    books = BookManager()


class Author(models.Model):
    name = models.CharField(max_length=100)


def chain_calls_return_the_queryset() -> None:
    assert_type(Author.objects.filter(), models.QuerySet[Author])
    assert_type(Author.objects.all().first(), Author | None)
    assert_type(Book.books.get_queryset(), BookQuerySet)
    assert_type(Book.books.filter(), BookQuerySet)
    assert_type(Book.books.order_by("pk").published(), BookQuerySet)
    assert_type(Book.books.select_related(None), BookQuerySet)
    assert_type(Book.books.get(pk=1), Book)


def count_rows(manager: models.Manager[Book]) -> int:
    return manager.count()


def custom_queryset_manager_is_still_a_manager() -> None:
    # The queryset parameter is covariant, so a narrower queryset still fits Manager[Book].
    count_rows(Book.books)



class ArticleQuerySet(models.QuerySet["Article"]):
    def drafts(self) -> "ArticleQuerySet":
        return self.filter(draft=True)


class Article(models.Model):
    draft = models.BooleanField()

    articles = ArticleQuerySet.as_manager()


def count_drafts(queryset: ArticleQuerySet) -> int:
    return queryset.drafts().count()


def count_articles(manager: models.Manager[Article]) -> int:
    return manager.count()


def as_manager_keeps_the_queryset_class() -> None:
    assert_type(Article.articles.get_queryset(), ArticleQuerySet)
    assert_type(Article.articles.filter().drafts(), ArticleQuerySet)
    assert_type(Article.articles.get(pk=1), Article)
    count_articles(Article.articles)


def as_manager_has_the_queryset_methods() -> None:
    # Only ty sees the queryset's own methods on the manager.
    assert_type(Article.articles.drafts(), ArticleQuerySet)  # type: ignore[attr-defined, assert-type]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType, reportAssertTypeFailure]
    count_drafts(Article.articles)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]


_M = TypeVar("_M", bound=models.Model)


class LiveManager(models.Manager[_M]):
    def live_count(self) -> int:
        return self.count()


class ReviewQuerySet(models.QuerySet["Review"]):
    def positive(self) -> "ReviewQuerySet":
        return self.filter(positive=True)


class Review(models.Model):
    positive = models.BooleanField()

    reviews = models.Manager.from_queryset(ReviewQuerySet)()
    live_reviews = LiveManager.from_queryset(ReviewQuerySet)()


def count_positive(queryset: ReviewQuerySet) -> int:
    return queryset.positive().count()


def from_queryset_keeps_the_manager_class() -> None:
    assert_type(Review.live_reviews.live_count(), int)


def from_queryset_has_the_queryset_methods() -> None:
    # Only ty sees the queryset's own methods on the manager.
    assert_type(Review.reviews.positive(), ReviewQuerySet)  # type: ignore[attr-defined, assert-type]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType, reportAssertTypeFailure]
    assert_type(Review.live_reviews.positive(), ReviewQuerySet)  # type: ignore[attr-defined, assert-type]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType, reportAssertTypeFailure]
    count_positive(Review.reviews)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]




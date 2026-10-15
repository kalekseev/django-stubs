from .base import run_pyright


def test_gettext_preserves_literal_string_only_for_literal_input() -> None:
    results = run_pyright(
        """\
from typing_extensions import Literal, LiteralString, assert_type
from django.utils.translation import gettext

assert_type(gettext("Enter your Social Security number."), LiteralString)

def check_messages(literal_message: LiteralString, dynamic_message: str) -> None:
    assert_type(gettext(literal_message), LiteralString)
    assert_type(gettext(dynamic_message), str)

def reject_dynamic_message(message: str) -> LiteralString:
    return gettext(message)

def reject_unchanged_literal() -> Literal["Hello"]:
    return gettext("Hello")
"""
    )
    errors = [result for result in results if result.type == "error"]
    assert [error.line for error in errors] == [11, 14]
    assert all("not assignable to return type" in error.message for error in errors)

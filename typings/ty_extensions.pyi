from typing import TypeVar

from typing_extensions import TypeAliasType

_Base = TypeVar("_Base")
_Extra = TypeVar("_Extra")

# Pyright and mypy use the base type. ty provides its own Intersection definition.
Intersection = TypeAliasType(
    "Intersection",
    _Base,
    type_params=(_Base, _Extra),
)

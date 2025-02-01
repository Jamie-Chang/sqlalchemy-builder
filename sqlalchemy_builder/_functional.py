"""Functional and type safe helpers."""
from dataclasses import dataclass
from functools import wraps
from typing import Callable, Concatenate, Generic, TypeVar

from typing_extensions import ParamSpec

T = TypeVar("T")
R = TypeVar("R")
P = ParamSpec("P")


@dataclass
class Pipeable(Generic[T, R]):
    """Wrap a callable and allow it to be involked with `|`.

    For example::
    >>> squared = Pipeable(lambda a: a * a)
    >>> 2 | squared
    4
    """

    fn: Callable[[T], R]

    def __call__(self, value: T) -> R:
        """Call the wrapped function."""
        return self.fn(value)

    def __ror__(self, value: T) -> R:
        """Use pipeline to call the wrapped function."""
        return self.fn(value)


def curry_and_swap(fn: Callable[Concatenate[T, P], R]) -> Callable[P, Pipeable[T, R]]:
    """Limited currying in Python.

    `func(x, y, z)` becomes `curry_and_swap(func)(y, z)(x)`
    Crucially the type information is preserved here.

    >>> def f(x, y, z):
    ...     return x * y + z
    >>> f(1, 2, 3) == curry_and_swap(f)(2, 3)(1)
    True
    """

    @wraps(fn)
    def _outer(*args: P.args, **kwargs: P.kwargs) -> Pipeable[T, R]:
        def _inner(first: T) -> R:
            return fn(first, *args, **kwargs)

        return Pipeable(_inner)

    return _outer

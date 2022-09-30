import copy
from typing import TypeVar
from .Unitbase import UnitBase

A = TypeVar("A", bound="Addition")

class Addition(UnitBase):
    def __init__(self, unit: float) -> None:
        super().__init__(unit)

    def __add__(self: A, other: A) -> A:
        clone = copy.copy(self)
        clone._unit = self._unit + other._unit
        return clone

    def __sub__(self: A, other: A) -> A:
        clone = copy.copy(self)
        clone._unit = self._unit - other._unit
        return clone

    def __neg__(self: A) -> A:
        clone = copy.copy(self)
        clone._unit = -self._unit
        return clone
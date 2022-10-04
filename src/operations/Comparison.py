import copy
import enum
from typing import Type, TypeVar
from .Unitbase import MetricBase, UnitBase

A = TypeVar("A", bound="Comparison")

class Comparison(UnitBase):
    def __init__(self, unit: float, metric: MetricBase) -> None:
        super().__init__(unit, metric)

    def __eq__(self, other: object) -> bool:
        if not type(other) == type(self) or not isinstance(other, Comparison):
            return False
        return self._unit == other._unit

    def __gt__(self: A, other: A) -> bool:
        return self._unit > other._unit

    def __ge__(self: A, other: A) -> bool:
        return self._unit >= other._unit

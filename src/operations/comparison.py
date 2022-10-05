from typing import TypeVar
from .unitbase import MetricBase, UnitBase

A = TypeVar("A", bound="Comparison")

class Comparison(UnitBase):
    '''
    Adds <, >, ==, >= and <= operations to the metric
    '''
    def __init__(self, unit: float, metric: MetricBase) -> None:
        UnitBase.__init__(self, unit, metric)

    def __eq__(self, other: object) -> bool:
        # pylint: disable=unidiomatic-typecheck
        if not type(other) == type(self) or not isinstance(other, Comparison):
            return False
        return self._unit == other._unit

    def __gt__(self: A, other: A) -> bool:
        return self._unit > other._unit

    def __ge__(self: A, other: A) -> bool:
        return self._unit >= other._unit

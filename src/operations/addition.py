import copy
from typing import TypeVar
from .unitbase import MetricBase, UnitBase

A = TypeVar("A", bound="Addition")

class Addition(UnitBase):
    '''
    Add +, - and negation operator to the metric
    '''
    def __init__(self, unit: float, metric: MetricBase) -> None:
        UnitBase.__init__(self, unit, metric)

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

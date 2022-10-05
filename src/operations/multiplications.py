from __future__ import annotations
import copy
from typing import Generic, Type, TypeVar, overload, Union, cast
from .unitbase import UnitBase, MetricBase

M = TypeVar("M", bound="UnitBase")
N = TypeVar("N", bound="UnitBase")
S = TypeVar("S", bound="UnitBase")

class DefaultMetric(MetricBase):
    '''
    don't use, only used for Multiplications
    '''
    DEFAULT = 1.0

class Multiplications(UnitBase, Generic[M, N]):
    '''
    Add multiplication operator to a metric
    works for both multiplications with numbers as with other metrics
    eg baseclass is A:
        A * float -> A
        A * M -> N
    '''
    def __init__(self, unit: float, metric: MetricBase, output: Type[N]) -> None:
        super().__init__(unit, metric)
        self.output = output

    @overload
    def __mul__(self: S, factor: M) -> N: ...
    @overload
    def __mul__(self: S, factor: float) -> S: ...

    def __mul__(self: S, factor: Union[float, int, M]) -> Union[S, N]:
        if isinstance(factor, (float, int)):
            clone = copy.copy(self)
            clone._unit = self._unit * factor
            return clone
        return cast(N, self.output(self._unit * factor._unit, DefaultMetric.DEFAULT))  # type: ignore

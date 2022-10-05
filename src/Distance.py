from __future__ import annotations
from typing import Union, overload
from src import Area
from src.operations.addition import Addition
from src.operations.comparison import Comparison
from src.operations.unitbase import UnitBase, MetricBase

class DistanceMetric(MetricBase):
    CM = 0.01
    DM = 0.1
    M = 1
    KM = 1000

M = DistanceMetric.M
DM = DistanceMetric.DM
CM = DistanceMetric.CM
KM = DistanceMetric.KM

class Distance(Comparison, Addition, UnitBase):
    def __init__(self, unit: float, metric: DistanceMetric) -> None:
        Comparison.__init__(self, unit=unit, metric=metric)

    def get(self, metric: DistanceMetric) -> float:
        return UnitBase._get(self, metric)

    def __str__(self) -> str:
        return f'{self._unit:1} m'

    @overload
    def __mul__(self, factor: float) -> 'Distance': ...
    @overload
    def __mul__(self, factor: 'Distance') -> Area.Area: ...

    def __mul__(self, factor: Union[float, 'Distance']) -> Union['Distance', Area.Area]:
        if isinstance(factor, float):
            return Distance(self._unit * factor, DistanceMetric.M)
        return Area.Area(self._unit * factor.get(DistanceMetric.M), Area.M2)

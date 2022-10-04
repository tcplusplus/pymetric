from __future__ import annotations
import enum
from typing import Union, overload
from src import Area
from src.operations.Unitbase import UnitBase, MetricBase

class DistanceMetric(MetricBase):
    CM = 0.01
    DM = 0.1
    M = 1
    KM = 1000

M = DistanceMetric.M
DM = DistanceMetric.DM
CM = DistanceMetric.CM
KM = DistanceMetric.KM

class Distance(UnitBase):
    def __init__(self, unit: float, metric: DistanceMetric) -> None:
        self.__meters = unit * metric.value
        UnitBase.__init__(self, unit=unit, default_metric=M)

    def get(self, metric: DistanceMetric) -> float:
        return self.__meters / metric.value

    def __str__(self) -> str:
        return f'{self.__meters:1} m'

    def __add__(self, other: 'Distance') -> 'Distance':
        meters = other.get(DistanceMetric.M)
        return Distance(meters + self.__meters, DistanceMetric.M)

    def __neg__(self) -> 'Distance':
        return Distance(-self.__meters, DistanceMetric.M)

    def __sub__(self, other: 'Distance') -> 'Distance':
        return self + (-other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            return False
        return self.__meters == other.__meters

    def __gt__(self, other: 'Distance') -> bool:
        return self.__meters > other.__meters

    def __ge__(self, other: 'Distance') -> bool:
        return self.__meters >= other.__meters

    @overload
    def __mul__(self, factor: float) -> 'Distance': ...
    @overload
    def __mul__(self, factor: 'Distance') -> Area.Area: ...

    def __mul__(self, factor: Union[float, 'Distance']) -> Union['Distance', Area.Area]:
        if isinstance(factor, float):
            return Distance(self.__meters * factor, DistanceMetric.M)
        return Area.Area(self.__meters * factor.get(DistanceMetric.M), Area.M2)

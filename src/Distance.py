import enum
from typing import Union, overload
from .Area import Area, AreaMetric

class DistanceMetric(enum.IntEnum):
    CM = -2
    DM = -1
    M = 0
    KM = 3

M = DistanceMetric.M
DM = DistanceMetric.DM
CM = DistanceMetric.CM
KM = DistanceMetric.KM

class Distance:
    def __init__(self, unit: float, metric: DistanceMetric) -> None:
        self.__meters = unit * (10.0 ** metric.value)

    def get(self, metric: DistanceMetric) -> float:
        return self.__meters / (10.0 ** metric.value)

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
    def __mul__(self, factor: 'Distance') -> Area: ...

    def __mul__(self, factor: Union[float, 'Distance']) -> Union['Distance', Area]:
        if isinstance(factor, float):
            return Distance(self.__meters * factor, DistanceMetric.M)
        return Area(self.__meters * factor.get(DistanceMetric.M), AreaMetric.M2)

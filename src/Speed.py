from __future__ import annotations
import enum
from typing import Union, overload
from src.operations.addition import Addition
from .Time import Time, Sec
from .Distance import Distance, M
from src import Acceleration

class SpeedMetric(enum.IntEnum):
    MpS = 10
    KMpH = 36

MpS = SpeedMetric.MpS
KMpH = SpeedMetric.KMpH

class Speed(Addition):
    def __init__(self, unit: float, metric: SpeedMetric) -> None:
        Addition.__init__(self, unit / (metric.value / 10.0))

    def get(self, metric: SpeedMetric) -> float:
        return self._unit * (metric.value / 10.0)

    @overload
    def __mul__(self, factor: float|int) -> 'Speed': ...
    @overload
    def __mul__(self, time: Time) -> Distance: ...

    def __mul__(self, factor: Union[float, int, Time]) -> Union['Speed', Distance]:
        if isinstance(factor, float) or isinstance(factor, int):
            return Speed(self._unit * factor, MpS)
        return Distance(self._unit * factor.get(Sec), M)

    @overload
    def __truediv__(self, factor: float|int) -> 'Speed': ...
    @overload
    def __truediv__(self, factor: Time) -> Acceleration.Acceleration: ...

    def __truediv__(self, factor: Union[float, int, Time]) -> Union['Speed', Acceleration.Acceleration]:
        if isinstance(factor, float) or isinstance(factor, int):
            return Speed(self._unit / factor, MpS)
        return Acceleration.Acceleration(self._unit / factor.get(Sec), Acceleration.MpS2)
from __future__ import annotations
import enum
from typing import Union, overload
from src.operations.addition import Addition
from .Time import Time, Sec
from .Speed import MpS, Speed

class AccelerationMetric(enum.IntEnum):
    MpS2 = 1

MpS2 = AccelerationMetric.MpS2

class Acceleration(Addition):
    def __init__(self, unit: float, metric: AccelerationMetric) -> None:
        Addition.__init__(self, unit / (metric.value / 1.0))

    def get(self, metric: AccelerationMetric) -> float:
        return self._unit * (metric.value / 1.0)

    @overload
    def __mul__(self, factor: float|int) -> 'Acceleration': ...
    @overload
    def __mul__(self, time: Time) -> Speed: ...

    def __mul__(self, factor: Union[float, int, Time]) -> Union['Acceleration', Speed]:
        if isinstance(factor, float) or isinstance(factor, int):
            return Acceleration(self._unit * factor, MpS2)
        return Speed(self._unit * factor.get(Sec), MpS)
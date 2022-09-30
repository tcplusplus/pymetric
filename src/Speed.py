from __future__ import annotations
import enum
from typing import Union, overload
from src.operations.addition import Addition
from .Time import Time, Sec
from .Distance import Distance, M

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
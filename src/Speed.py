from __future__ import annotations
from email.policy import default
import enum
from typing import Union, overload
from src.operations.Addition import Addition
from src.operations.Multiplications import Multiplications
from src.operations.Unitbase import MetricBase
from .Time import Time, Sec
from .Distance import Distance, M
from src import Acceleration

class SpeedMetric(MetricBase):
    MpS = 1
    KMpH = 1/3.6

MpS = SpeedMetric.MpS
KMpH = SpeedMetric.KMpH

class Speed(Addition, Multiplications[Time, Distance]):
    def __init__(self, unit: float, metric: SpeedMetric) -> None:
        Multiplications.__init__(self, unit, metric=metric, output=Distance)

    def get(self, metric: SpeedMetric) -> float:
        return super().get(metric=metric)


    @overload
    def __truediv__(self, factor: float|int) -> 'Speed': ...
    @overload
    def __truediv__(self, factor: Time) -> Acceleration.Acceleration: ...

    def __truediv__(self, factor: Union[float, int, Time]) -> Union['Speed', Acceleration.Acceleration]:
        if isinstance(factor, float) or isinstance(factor, int):
            return Speed(self._unit / factor, MpS)
        return Acceleration.Acceleration(self._unit / factor.get(Sec), Acceleration.MpS2)
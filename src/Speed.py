from __future__ import annotations
from email.policy import default
import enum
from typing import Union, overload
from src.operations.Addition import Addition
from src.operations.Multiplications import Multiplications
from .Time import Time, Sec
from .Distance import Distance, M
from src import Acceleration

class SpeedMetric(float, enum.Enum):
    MpS = 1
    KMpH = 3.6

MpS = SpeedMetric.MpS
KMpH = SpeedMetric.KMpH

class Speed(Addition, Multiplications[Time, Distance]):
    def __init__(self, unit: float, metric: SpeedMetric) -> None:
        Multiplications.__init__(self, unit / metric.value, default_metric=MpS, output=Distance)

    def get(self, metric: SpeedMetric) -> float:
        return self._unit * metric.value

    '''
    @overload
    def __mul__(self, factor: float|int) -> 'Speed': ...
    @overload
    def __mul__(self, time: Time) -> Distance: ...

    def __mul__(self, factor: Union[float, int, Time]) -> Union['Speed', Distance]:
        if isinstance(factor, float) or isinstance(factor, int):
            return Speed(self._unit * factor, MpS)
        return Distance(self._unit * factor.get(Sec), M)
    '''

    @overload
    def __truediv__(self, factor: float|int) -> 'Speed': ...
    @overload
    def __truediv__(self, factor: Time) -> Acceleration.Acceleration: ...

    def __truediv__(self, factor: Union[float, int, Time]) -> Union['Speed', Acceleration.Acceleration]:
        if isinstance(factor, float) or isinstance(factor, int):
            return Speed(self._unit / factor, MpS)
        return Acceleration.Acceleration(self._unit / factor.get(Sec), Acceleration.MpS2)
from __future__ import annotations
from typing import Union, overload
from src.operations.addition import Addition
from src.operations.multiplications import Multiplications
from src.operations.unitbase import MetricBase, UnitBase
from src import acceleration, time, distance

class SpeedMetric(MetricBase):
    '''
    Metrics of speed
    options are m/s or km/h
    '''
    MPS = 1
    KMPH = 1/3.6

MpS = SpeedMetric.MPS
KMpH = SpeedMetric.KMPH

class Speed(Addition, Multiplications[time.Time, distance.Distance], UnitBase):
    '''
    A metric represenation of speed
    '''
    def __init__(self, unit: float, metric: SpeedMetric) -> None:
        Addition.__init__(self, unit, metric)
        Multiplications.__init__(self, unit, metric=metric, output=distance.Distance)
        UnitBase.__init__(self, unit, metric)

    def get(self, metric: SpeedMetric) -> float:
        return UnitBase._get(self, metric=metric)


    @overload
    def __truediv__(self, factor: float|int) -> 'Speed': ...
    @overload
    def __truediv__(self, factor: time.Time) -> acceleration.Acceleration: ...

    def __truediv__(self, factor: Union[float, int, time.Time]) -> Union['Speed', acceleration.Acceleration]:
        if isinstance(factor, (float, int)):
            return Speed(self._unit / factor, MpS)
        return acceleration.Acceleration(self._unit / factor.get(time.Sec), acceleration.MpS2)

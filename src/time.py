from __future__ import annotations
from typing import Union, overload
from src import distance, speed
from src.operations.unitbase import MetricBase, UnitBase

from .operations.addition import Addition

class TimeMetric(MetricBase):
    '''
    Metrics representation of time eg msec, sec, min, hour
    '''
    MSEC = 0.001
    SEC = 1
    MIN = 60
    HOUR = 3600

MSec = TimeMetric.MSEC
Sec = TimeMetric.SEC
Min = TimeMetric.MIN
Hour = TimeMetric.HOUR

class Time(Addition, UnitBase):
    '''
    A metric representation of time
    '''
    def __init__(self, unit: float, metric: TimeMetric) -> None:
        Addition.__init__(self, unit, metric=metric)
        UnitBase.__init__(self, unit, metric=metric)

    def get(self, metric: TimeMetric) -> float:
        return UnitBase._get(self, metric)

    @overload
    def __mul__(self, factor: float) -> 'Time': ...
    @overload
    def __mul__(self, factor: speed.Speed) -> distance.Distance: ...

    def __mul__(self, factor: Union[speed.Speed, float]) -> Union[distance.Distance, 'Time']:
        if isinstance(factor, float):
            return Time(self._unit * factor, Sec)
        return distance.Distance(self._unit * factor.get(speed.MpS), distance.M)

    def __truediv__(self, factor: float) -> 'Time':
        return Time(self._unit / factor, Sec)

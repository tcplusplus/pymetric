from __future__ import annotations
from typing import Union, overload
from src import Speed, Distance
from src.operations.unitbase import MetricBase, UnitBase

from .operations.addition import Addition

class TimeMetric(MetricBase):
    MSec = 0.001
    Sec = 1
    Min = 60
    Hour = 3600

MSec = TimeMetric.MSec
Sec = TimeMetric.Sec
Min = TimeMetric.Min
Hour = TimeMetric.Hour

class Time(Addition, UnitBase):
    def __init__(self, unit: float, metric: TimeMetric) -> None:
        Addition.__init__(self, unit, metric=metric)

    def get(self, metric: TimeMetric) -> float:
        return UnitBase._get(self, metric)

    @overload
    def __mul__(self, factor: float) -> 'Time': ...
    @overload
    def __mul__(self, speed: Speed.Speed) -> Distance.Distance: ...

    def __mul__(self, factor: Union[Speed.Speed, float]) -> Union[Distance.Distance, 'Time']:
        if isinstance(factor, float):
            return Time(self._unit * factor, TimeMetric.Sec)
        return Distance.Distance(self._unit * factor.get(Speed.MpS), Distance.M)

    def __truediv__(self, factor: float) -> 'Time':
        return Time(self._unit / factor, TimeMetric.Sec)
from __future__ import annotations
from src import Speed, Time
from src.operations import addition, comparison, multiplications, unitbase

class AccelerationMetric(unitbase.MetricBase):
    MpS2 = 1

MpS2 = AccelerationMetric.MpS2

class Acceleration(multiplications.Multiplications[Time.Time, 'Speed.Speed'], addition.Addition, comparison.Comparison):
    def __init__(self, unit: float, metric: AccelerationMetric) -> None:
        multiplications.Multiplications.__init__(self, unit, metric=metric, output=Speed.Speed)

    def get(self, metric: AccelerationMetric) -> float:
        return unitbase.UnitBase._get(self, metric)

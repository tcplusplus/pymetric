from __future__ import annotations
from src import Speed, Time
from src.operations import Multiplications, Addition, Unitbase, Comparison

class AccelerationMetric(Unitbase.MetricBase):
    MpS2 = 1

MpS2 = AccelerationMetric.MpS2

class Acceleration(Multiplications.Multiplications[Time.Time, 'Speed.Speed'], Addition.Addition, Comparison.Comparison):
    def __init__(self, unit: float, metric: AccelerationMetric) -> None:
        Multiplications.Multiplications.__init__(self, unit, metric=metric, output=Speed.Speed)

    def get(self, metric: AccelerationMetric) -> float:
        return super().get(metric)

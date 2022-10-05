from __future__ import annotations
from src import speed, time
from src.operations import addition, comparison, multiplications
from src.operations.unitbase import UnitBase, MetricBase

class AccelerationMetric(MetricBase):
    '''
    Metric for acceleration: eg m/s^2
    '''
    MPS2 = 1

MpS2 = AccelerationMetric.MPS2

class Acceleration(multiplications.Multiplications[time.Time, 'speed.Speed'],
                   addition.Addition,
                   comparison.Comparison,
                   UnitBase):
    '''
    A represenation for an acceleration
    '''
    def __init__(self, unit: float, metric: AccelerationMetric) -> None:
        multiplications.Multiplications.__init__(self, unit, metric=metric, output=speed.Speed)
        addition.Addition.__init__(self, unit, metric)
        comparison.Comparison.__init__(self, unit, metric)
        UnitBase.__init__(self, unit, metric)

    def get(self, metric: AccelerationMetric) -> float:
        return UnitBase._get(self, metric)

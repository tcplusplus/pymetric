from __future__ import annotations
from src.operations.comparison import Comparison
from src.operations.addition import Addition
from src.operations.unitbase import MetricBase, UnitBase
from src.operations.display import Display

class AreaMetric(MetricBase):
    '''
    Metric for an Area eg: m^2, dm^2, cm^2, mm^2
    '''
    M2 = 1
    DM2 = 0.01
    CM2 = 0.0001
    MM2 = 0.000001

M2 = AreaMetric.M2
DM2 = AreaMetric.DM2
CM2 = AreaMetric.CM2
MM2 = AreaMetric.MM2


class Area(Comparison, Addition, Display, UnitBase):
    '''
    A metric representation for an Area
    '''
    def __init__(self, unit: float, metric: AreaMetric) -> None:
        Comparison.__init__(self, unit=unit, metric=metric)
        Addition.__init__(self, unit=unit, metric=metric)
        Display.__init__(self, unit=unit, metric=metric, default_metric='m2')
        UnitBase.__init__(self, unit=unit, metric=metric)

    def get(self, metric: AreaMetric) -> float:
        return UnitBase._get(self, metric)

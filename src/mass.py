from __future__ import annotations
from src.operations.addition import Addition
from src.operations.comparison import Comparison
from src.operations.unitbase import MetricBase, UnitBase

class MassMetric(MetricBase):
    '''
    Metrics for mass. eg: mg, g, Kg, T
    '''
    MG = 0.001
    G = 1
    KG = 1000
    T = 1000_000

MG = MassMetric.MG
G = MassMetric.G
KG = MassMetric.KG
T = MassMetric.T

class Mass(Comparison, Addition, UnitBase):
    '''
    Metrics representation of a mass
    '''
    def __init__(self, unit: float, metric: MassMetric) -> None:
        Comparison.__init__(self, unit, metric=metric)
        Addition.__init__(self, unit, metric=metric)
        UnitBase.__init__(self, unit, metric=metric)

    def get(self, metric: MassMetric) -> float:
        return UnitBase._get(self, metric=metric)

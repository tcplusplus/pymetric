from __future__ import annotations
from src.operations import Comparison
from src.operations.Addition import Addition
from src.operations.Unitbase import MetricBase, UnitBase

class AreaMetric(MetricBase):
    M2 = 1
    DM2 = 0.01
    CM2 = 0.0001
    MM2 = 0.000001

M2 = AreaMetric.M2
DM2 = AreaMetric.DM2
CM2 = AreaMetric.CM2
MM2 = AreaMetric.MM2


class Area(Addition, UnitBase):
    def __init__(self, unit: float, metric: AreaMetric) -> None:
       Addition.__init__(self, unit, metric)

    def get(self, metric: AreaMetric) -> float:
        return super().get(metric)

    def __str__(self) -> str:
        return f'{self._unit:1} m2'
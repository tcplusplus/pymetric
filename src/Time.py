import enum

from .operations.addition import Addition
from .operations.multiplications import Multiplications

class TimeMetric(enum.IntEnum):
    MSec = 0.001
    Sec = 1
    Min = 60
    Hour = 3600

MSec = TimeMetric.MSec
Sec = TimeMetric.Sec
Min = TimeMetric.Min
Hour = TimeMetric.Hour

class Time(Multiplications, Addition):
    def __init__(self, unit: float, metric: TimeMetric) -> None:
        Multiplications.__init__(self, unit * metric.value)
        Addition.__init__(self, unit * metric.value)

    def get(self, metric: TimeMetric) -> float:
        return self._unit / metric.value

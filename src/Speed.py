import enum

from .operations.addition import Addition
from .Time import Sec, Time
from .Distance import Distance, DistanceMetric

class SpeedMetric(enum.IntEnum):
    MpS = 10
    KMpH = 36

MpS = SpeedMetric.MpS
KMpH = SpeedMetric.KMpH

class Speed(Addition):
    def __init__(self, unit: float, metric: SpeedMetric) -> None:
        Addition.__init__(self, unit / (metric.value / 10.0))

    def get(self, metric: SpeedMetric) -> float:
        return self._unit * (metric.value / 10.0)

    def __mul__(self, time: Time) -> Distance:
        return Distance(self._unit * time.get(Sec), DistanceMetric.M)
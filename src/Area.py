from __future__ import annotations
import enum

class AreaMetric(enum.IntEnum):
    M2 = 0
    DM2 = -2
    CM2 = -4
    MM2 = -6

M2 = AreaMetric.M2
DM2 = AreaMetric.DM2
CM2 = AreaMetric.CM2
MM2 = AreaMetric.MM2


class Area:
    def __init__(self, unit: float, metric: AreaMetric) -> None:
        self.__square_meters = unit * (10.0 ** metric.value)

    def get(self, metric: AreaMetric) -> float:
        return self.__square_meters / (10.0 ** metric.value)

    def __str__(self) -> str:
        return f'{self.__square_meters:1} m2'
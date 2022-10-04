from abc import abstractmethod
import enum
from re import I
from typing import Generic, TypeVar

class MetricBase(float, enum.Enum):
    pass

class UnitBase():
    def __init__(self, unit: float, default_metric: MetricBase) -> None:
        self._unit = unit
        self._default_metric = default_metric

    @abstractmethod
    def get(self, metric: MetricBase) -> float: ...
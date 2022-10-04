from abc import abstractmethod
import enum
from re import I
from typing import Generic, TypeVar

class MetricBase(float, enum.Enum):
    pass

class UnitBase():
    def __init__(self, unit: float, metric: MetricBase) -> None:
        self._unit = unit * metric

    @abstractmethod
    def get(self, metric: MetricBase) -> float:
        return self._unit / metric
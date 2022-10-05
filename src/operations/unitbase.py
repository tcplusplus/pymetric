from abc import abstractmethod
import enum

class MetricBase(float, enum.Enum):
    '''
    default value is 1.0 for standard metric and for all other options it gives the factor to that default metric
    eg:
      Meter = 1
      MilliMeter = 0.001
      KiloMeter = 1000
    '''

class UnitBase():
    '''
    Represents a metric from the metric system.
    Consists of a unit and a metric
    '''
    def __init__(self, unit: float, metric: MetricBase) -> None:
        self._unit = unit * metric

    def _get(self, metric: MetricBase) -> float:
        return self._unit / metric

from .unitbase import MetricBase, UnitBase

class Display(UnitBase):
    '''
    Adds str and repr operator to the metric
    '''
    def __init__(self, unit: float, metric: MetricBase, default_metric: str) -> None:
        super().__init__(unit, metric)
        self._default_metric = default_metric

    def __str__(self) -> str:
        return f'{self._unit} {self._default_metric}'

    def __repr__(self) -> str:
        return str(self)

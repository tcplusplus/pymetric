import copy
import enum
from typing import Generic, Type, TypeVar, overload, Union, cast
from .Unitbase import UnitBase, MetricBase

M = TypeVar("M", bound="UnitBase")
N = TypeVar("N", bound="UnitBase")
S = TypeVar("S", bound="UnitBase")

class DefaultMetric(MetricBase):
    default = 1.0


class Multiplications(UnitBase, Generic[M, N]):
    def __init__(self, unit: float, default_metric: MetricBase, output: Type[N]) -> None:
        super().__init__(unit, default_metric)
        self.output = output

    @overload
    def __mul__(self: S, factor: M) -> N: ...
    @overload
    def __mul__(self: S, factor: float) -> S: ...

    def __mul__(self: S, factor: Union[float, int, M]) -> Union[S, N]:
        if isinstance(factor, float) or isinstance(factor, int):
            clone = copy.copy(self)
            clone._unit = self._unit * factor
            return clone
        return cast(N, self.output(self._unit * factor._unit, DefaultMetric.default))  # type: ignore

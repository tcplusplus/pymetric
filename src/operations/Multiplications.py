import copy
from typing import TypeVar
from .Unitbase import UnitBase

M = TypeVar("M", bound="Multiplications")

class Multiplications(UnitBase):
    def __init__(self, unit: float) -> None:
        super().__init__(unit)

    def __mul__(self: M, factor: float) -> M:
        clone = copy.copy(self)
        clone._unit = self._unit * factor
        return clone

    def __truediv__(self: M, factor: float) -> M:
        clone = copy.copy(self)
        clone._unit = self._unit / factor
        return clone
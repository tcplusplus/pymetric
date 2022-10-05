import math
from typing import Literal
from .Area import MM2, Area
from .Distance import M, Distance
from .results.result import Failure, Result, Success

def sqrt(area: Area) -> Result[Distance, Literal['negative']]:
    mm2 = area.get(MM2)
    if mm2 < 0:
        return Failure('negative', 'area cannot be negative')
    return Success(Distance(math.sqrt(mm2), M))
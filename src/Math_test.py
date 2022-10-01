from src.Distance import M
from .Area import Area, MM2
from .Math import sqrt

class TestMath:
    def test_sqrt_of_area(self) -> None:
        area = Area(4, MM2)
        dist = sqrt(area)
        assert dist.is_success
        if dist.is_success:
            assert dist.value.get(M) == 2

    def test_sqrt_of_neg_area(self) -> None:
        area = Area(-4, MM2)
        dist = sqrt(area)
        assert dist.is_failure
        if dist.is_failure:
            assert dist.error_code == 'negative'
            assert dist.message == 'area cannot be negative'
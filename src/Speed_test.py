from .Speed import Speed, MpS, KMpH
from .Time import Time, Hour
from .Distance import KM
import pytest

class TestSpeed:
    def test_speed_type(self) -> None:
        speed = Speed(10, MpS)
        assert speed.get(MpS) == 10

    def test_convert_from_mps_to_kmh(self) -> None:
        speed = Speed(10, MpS)
        assert speed.get(KMpH) == 36

    def test_add_speeds(self) -> None:
        speed = Speed(4, MpS) + Speed(3, MpS)
        assert speed.get(MpS) == 7

    def test_subtract_speeds(self) -> None:
        speed = Speed(4, MpS) - Speed(3, MpS)
        assert speed.get(MpS) == 1

    def test_neg_speed(self) -> None:
        speed = -Speed(3, MpS)
        assert speed.get(MpS) == -3

    def test_speed_times_time_is_distance(self) -> None:
        distance = Speed(3, KMpH) * Time(2, Hour)
        assert pytest.approx(distance.get(KM), 0.001)  == 6
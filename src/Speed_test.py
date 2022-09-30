from .Speed import Speed, MpS, KMpH
from .Time import Time, Hour, Sec
from .Acceleration import Acceleration, MpS2
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

    def test_speed_can_be_multiplied(self) -> None:
        speed = Speed(3, KMpH) * 2.0
        assert speed.get(KMpH) == 6

    def test_speed_can_be_multiplied_by_int(self) -> None:
        speed = Speed(3, KMpH) * 2
        assert speed.get(KMpH) == 6

    def test_speed_can_be_divided(self) -> None:
        speed = Speed(4, KMpH) / 2
        assert speed.get(KMpH) == 2

    def test_divide_speed_by_time_gives_acceleration(self) -> None:
        acc = Speed(4, MpS) / Time(2, Sec)
        assert acc.get(MpS2) == 2
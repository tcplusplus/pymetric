from .Distance import KM
from .Speed import KMpH, Speed
from .Time import Hour, Time, Sec, Min
import pytest


class TestTime:
    def test_time_class(self) -> None:
        time = Time(12, Sec)
        assert time.get(Sec) == 12

    def test_convert_seconds_to_minutes(self) -> None:
        time = Time(120, Sec)
        assert time.get(Min) == 2

    def test_adding_up_times(self) -> None:
        time = Time(3, Sec) + Time(2, Min)
        assert time.get(Sec) == 123

    def test_negation_of_time(self) -> None:
        time = Time(4, Sec)
        assert (-time).get(Sec) == -4

    def test_subtracting_time(self) -> None:
        time = Time(2, Min) - Time(4, Sec)
        assert time.get(Sec) == 116

    def test_time_multiplication(self) -> None:
        time = Time(2, Min) * 2.0
        assert time.get(Min) == 4

    def test_time_devision(self) -> None:
        time = Time(2, Min) / 2.0
        assert time.get(Min) == 1

    '''
    def test_time_times_speed_is_distance(self) -> None:
        distance = Time(2, Hour) * Speed(3, KMpH)
        assert pytest.approx(distance.get(KM), 0.001)  == 6
    '''
from src.speed import MpS
from src.time import Sec, Time
from .acceleration import Acceleration, MpS2

class TestAcceleration:
    '''
    pytest to test Acceleration Class
    '''
    def test_acceleration(self) -> None:
        acc = Acceleration(4, MpS2)
        assert acc.get(MpS2) == 4

    def test_acceleration_addition(self) -> None:
        acc = Acceleration(2, MpS2) + Acceleration(4, MpS2)
        assert acc.get(MpS2) == 6

    def test_acceleration_subtraction(self) -> None:
        acc = Acceleration(2, MpS2) - Acceleration(4, MpS2)
        assert acc.get(MpS2) == -2

    def test_acceleration_negation(self) -> None:
        acc = -Acceleration(4, MpS2)
        assert acc.get(MpS2) == -4

    def test_acceleration_multiplication(self) -> None:
        acc = Acceleration(4, MpS2) * 3
        assert acc.get(MpS2) == 12

    def test_acceleration_times_time_is_speed(self) -> None:
        speed = Acceleration(4, MpS2) * Time(2, Sec)
        assert speed.get(MpS) == 8

    def test_check_acceleration_comparisons(self) -> None:
        assert Acceleration(4, MpS2) > Acceleration(3, MpS2)

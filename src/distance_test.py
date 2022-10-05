from src.area import AreaMetric
from .speed import Speed, MpS
from .distance import Distance, M, CM, KM

class TestDistance:
    '''
    pytest to test distances
    '''
    def test_create_meters(self) -> None:
        distance = Distance(unit=4, metric=M)
        assert distance.get(M) == 4

    def test_convert_to_cm(self) -> None:
        distance = Distance(unit=6.5, metric=M)
        assert distance.get(CM) == 650

    def test_cannot_assign_meters_to_float(self) -> None:
        # pylint: disable=unused-variable
        not_used: int = Distance(unit=3, metric=M)   # type: ignore

    def test_convert_cm_to_km(self) -> None:
        distance = Distance(unit=12345, metric=CM)
        assert distance.get(KM) == 0.12345

    def test_distance_to_string(self) -> None:
        distance = Distance(unit=4, metric=M)
        rep = str(distance)
        assert rep == '4.0 m'

    def test_adding_2_distances(self) -> None:
        distance = Distance(unit=6.5, metric=M)
        new_distance = distance + Distance(unit=2, metric=KM)
        assert new_distance.get(M) == 2006.5

    def test_compare_cannot_be_between_different_metrics(self) -> None:
        distance = Distance(unit=3, metric=M)
        speed = Speed(3, MpS)
        assert distance != speed

    def test_cannot_add_distance_with_number(self) -> None:
        distance = Distance(unit=6.5, metric=M)
        try:
            # pylint: disable=unused-variable
            new_distance = distance + 5  # type: ignore
        # pylint: disable=bare-except
        except:
            pass

    def test_multiplication_with_number(self) -> None:
        distance = Distance(unit=6.5, metric=M)
        new_distance = distance * 2.0
        assert new_distance.get(metric=M) == 13

    def test_multiply_with_distance_returns_area(self) -> None:
        distance1 = Distance(unit=2, metric=M)
        distance2 = Distance(unit=3, metric=M)
        area = distance1 * distance2
        assert area.get(AreaMetric.M2) == 6

    def test_distances_can_be_negated(self) -> None:
        distance = -Distance(4, M)
        assert distance.get(M) == -4

    def test_subtraction_of_distances(self) -> None:
        distance = Distance(3, M) - Distance(50, CM)
        assert distance.get(M) == 2.5

    def test_2_distance_are_the_same(self) -> None:
        distance1 = Distance(3, M)
        distance2 = Distance(3, M)
        assert distance1 == distance2

    def test_2_distance_are_not_the_same(self) -> None:
        distance1 = Distance(3, M)
        distance2 = Distance(4, M)
        assert distance1 != distance2

    def test_distance_equation(self) -> None:
        distance1 = Distance(3, M)
        distance2 = Distance(4, M)
        assert distance1 < distance2
        assert distance2 >= distance1

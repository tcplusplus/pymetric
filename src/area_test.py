from .area import Area, M2, MM2, CM2, DM2

class TestArea:
    '''
    pytest to test Area Metrics
    '''
    def test_create_area(self) -> None:
        area = Area(3, M2)
        assert area.get(M2) == 3

    def test_convert_m2_to_mm2(self) -> None:
        area = Area(4, M2)
        assert area.get(MM2) == 4_000_000

    def test_convert_cm2_to_dm2(self) -> None:
        area = Area(4, CM2)
        assert area.get(DM2) == 0.04

    def test_area_to_string(self) -> None:
        area = Area(3.5, M2)
        assert str(area) == '3.5 m2'

    def test_addition_between_areas(self) -> None:
        area = Area(2, M2) + Area(50, DM2)
        assert area.get(M2) == 2.5

    def test_comparisons(self) -> None:
        assert Area(2, M2) < Area(3, M2)

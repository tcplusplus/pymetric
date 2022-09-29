from .Area import Area, M2, MM2, CM2, DM2


class TestArea:
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
        print('something')
        assert str(area) == '3.5 m2'
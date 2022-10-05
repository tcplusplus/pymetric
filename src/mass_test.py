from src.mass import Mass, KG, G

class TestMass:
    '''
    pytests for the Mass Class
    '''
    def test_create_mass(self) -> None:
        mass = Mass(3.2, KG)
        assert mass.get(G) == 3200

    def test_mass_addition(self) -> None:
        mass = Mass(3, KG) + Mass(300, G)
        assert mass.get(G) == 3_300

    def test_mass_comparison(self) -> None:
        assert Mass(3, KG) >= Mass(3, KG)

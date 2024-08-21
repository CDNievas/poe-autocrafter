import pathlib

from src.utils.parser import Parser

class Test:

    item = None

    @classmethod
    def setup_class(cls):
        path = pathlib.Path("tests/parser/files/weapon_2h_unique_double_6l_6_20_none_no_0_yes_yes_poe.txt")
        file = open(path, "r")
        text = file.read()
        
        cls.item = Parser.parse(text)

    def test_item_class(cls):
        assert cls.item.item_class == "Two Hand Swords"

    def test_rarity(cls):
        assert cls.item.rarity == "Unique"

    def test_ilvl(cls):
        assert cls.item.ilvl == 71

    def test_quality(cls):
        assert cls.item.quality == 20

    def test_physical_damage(cls):

        asserts = []

        asserts.append(cls.item.physical_dmg["min"] == 49)
        asserts.append(cls.item.physical_dmg["max"] == 102)

        assert all(asserts)

    def test_critical_strike_chance(cls):
        assert cls.item.critical_strike_chance == 5

    def test_attacks_per_second(cls):
        assert cls.item.attacks_per_second == 1.59

    def test_weapon_range(cls):
        assert cls.item.weapon_range == 1.3

    def test_requirements(cls):

        asserts = []

        asserts.append(cls.item.requirements["level"] == 48)
        asserts.append(cls.item.requirements["str"] == 91)
        asserts.append(cls.item.requirements["dex"] == 76)
        asserts.append(cls.item.requirements["int"] == 0)

        assert all(asserts)

    def test_sockets(cls):

        asserts = []
        asserts.append(cls.item.sockets == "G-G-R-R-R-G")
        asserts.append(cls.item.links == 6)

        assert all(asserts)

    def test_mods(cls):
        
        assert len(cls.item.mods) == 8
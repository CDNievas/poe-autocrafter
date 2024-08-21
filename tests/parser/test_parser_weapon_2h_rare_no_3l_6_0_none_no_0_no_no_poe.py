import pathlib

from src.utils.parser import Parser

class Test:

    item = None

    @classmethod
    def setup_class(cls):
        path = pathlib.Path("tests/parser/files/weapon_2h_rare_no_3l_6_0_none_no_0_no_no_poe.txt")
        file = open(path, "r")
        text = file.read()
        
        cls.item = Parser.parse(text)

    def test_item_class(cls):
        assert cls.item.item_class == "Two Hand Axes"

    def test_rarity(cls):
        assert cls.item.rarity == "Rare"

    def test_ilvl(cls):
        assert cls.item.ilvl == 73

    def test_quality(cls):
        assert cls.item.quality == 0

    def test_physical_damage(cls):

        asserts = []

        asserts.append(cls.item.physical_dmg["min"] == 133)
        asserts.append(cls.item.physical_dmg["max"] == 213)

        assert all(asserts)

    def test_critical_strike_chance(cls):
        assert cls.item.critical_strike_chance == 5

    def test_attacks_per_second(cls):
        assert cls.item.attacks_per_second == 1.05

    def test_weapon_range(cls):
        assert cls.item.weapon_range == 1.3

    def test_requirements(cls):

        asserts = []

        asserts.append(cls.item.requirements["level"] == 58)
        asserts.append(cls.item.requirements["str"] == 102)
        asserts.append(cls.item.requirements["dex"] == 29)
        asserts.append(cls.item.requirements["int"] == 0)

        assert all(asserts)

    def test_sockets(cls):

        asserts = []
        asserts.append(cls.item.sockets == "R-R-R G-B-R")
        asserts.append(cls.item.links == 3)

        assert all(asserts)

    def test_mods(cls):
        
        assert len(cls.item.mods) == 5
import pathlib

from src.utils.parser import Parser

class Test:

    item = None

    @classmethod
    def setup_class(cls):
        path = pathlib.Path("tests/parser/files/weapon_2h_rare_no_1l_1_0_none_no_1_yes_no_poe.txt")
        file = open(path, "r")
        text = file.read()
        
        cls.item = Parser.parse(text)

    def test_item_class(cls):
        assert cls.item.item_class == "Two Hand Axes"

    def test_rarity(cls):
        assert cls.item.rarity == "Rare"

    def test_ilvl(cls):
        assert cls.item.ilvl == 66

    def test_quality(cls):
        assert cls.item.quality == 0

    def test_physical_damage(cls):

        asserts = []

        asserts.append(cls.item.physical_dmg["min"] == 202)
        asserts.append(cls.item.physical_dmg["max"] == 338)

        assert all(asserts)

    def test_critical_strike_chance(cls):
        assert cls.item.critical_strike_chance == 5.65

    def test_attacks_per_second(cls):
        assert cls.item.attacks_per_second == 1.27

    def test_weapon_range(cls):
        assert cls.item.weapon_range == 1.3

    def test_requirements(cls):

        asserts = []

        asserts.append(cls.item.requirements["level"] == 64)
        asserts.append(cls.item.requirements["str"] == 158)
        asserts.append(cls.item.requirements["dex"] == 76)
        asserts.append(cls.item.requirements["int"] == 0)

        assert all(asserts)

    def test_sockets(cls):

        asserts = []
        asserts.append(cls.item.sockets == "R")
        asserts.append(cls.item.links == 1)

        assert all(asserts)

    def test_mods(cls):
        
        assert len(cls.item.mods) == 7
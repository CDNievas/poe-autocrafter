import pathlib

from src.utils.parser import Parser

class Test:

    item = None

    @classmethod
    def setup_class(cls):
        path = pathlib.Path("tests/parser/files/body_armour_rare_no_1l_1_0_none_no_1_yes_no_poe.txt")
        file = open(path, "r")
        text = file.read()
        
        cls.item = Parser.parse(text)

    def test_item_class(cls):
        assert cls.item.item_class == "Body Armours"

    def test_rarity(cls):
        assert cls.item.rarity == "Rare"

    def test_ilvl(cls):
        assert cls.item.ilvl == 72

    def test_quality(cls):
        assert cls.item.quality == 0

    def test_armour(cls):
        assert cls.item.armour == 0

    def test_evasion_rating(cls):
        assert cls.item.evasion_rating == 1379

    def test_energy_shield(cls):
        assert cls.item.energy_shield == 0

    def test_requirements(cls):

        asserts = []

        asserts.append(cls.item.requirements["level"] == 68)
        asserts.append(cls.item.requirements["str"] == 0)
        asserts.append(cls.item.requirements["dex"] == 183)
        asserts.append(cls.item.requirements["int"] == 0)

        assert all(asserts)

    def test_sockets(cls):

        asserts = []
        asserts.append(cls.item.sockets == "G")
        asserts.append(cls.item.links == 1)

        assert all(asserts)

    def test_mods(cls):
        
        assert len(cls.item.mods) == 8
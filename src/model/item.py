class Item:

    def __init__(self):
        # Base
        self.item_class = ""
        self.rarity = ""
        self.ilvl = 0
        self.quality = 0
        
        # Armour Stats
        self.armour = 0
        self.energy_shield = 0
        self.evasion_rating = 0

        # Weapon Stats
        self.physical_dmg = {
            "max":0,
            "min":0
        }
        self.elemental_damage = {
            "fire":{
                "max":0,
                "min":0
            },
            "cold":{
                "max":0,
                "min":0
            },
            "lightning":{
                "max":0,
                "min":0
            }
        }
        self.critical_strike_chance = 0
        self.attacks_per_second = 0
        self.weapon_range = 0

        # Requirements
        self.requirements = {
            "level": 0,
            "int": 0,
            "dex": 0,
            "str": 0
        }

        # Sockets
        self.sockets = ""
        self.links = 0

        # Mods
        self.mods = []
        #self.enchanted_mods = []
        #self.implicit_mods = []
        #self.corrupted_mods = []
        #self.fractured_mods = []
        #self.crafted_mods = []
        #self.common_mods = []

        # Item
        self.corrupted = False
        self.fractured = False
        self.enchanted = False
        self.influenced_search = False
        self.influenced_eater = False







import re

from src.model.item import Item

class Parser:

    @staticmethod
    def parse(text: str):
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        item = Item()

        sections = text.split("--------\n")
        
        # Base
        match = re.search(r'Item Class:\s*(.+)', sections[0])
        if match:
            item.item_class = match.group(1).replace("\n", "")
        
        match = re.search(r"Rarity:\s*(.*)", sections[0])
        if match:
            item.rarity = match.group(1).replace("\n", "")

        match = re.search(r'Item Level:\s*(\d+(\.\d+)?)', sections[4])
        if match:
            item.ilvl = int(match.group(1))

        match = re.search(r"Quality:\s*([+-]?\d+)", sections[1])
        print(match)
        if match:
            item.quality = int(match.group(1))

        # Stats
        match = re.search(r'Evasion Rating:\s*(\d+(\.\d+)?)', sections[1])
        if match:
            item.evasion_rating = int(match.group(1))
        
        match = re.search(r'Armour:\s*(\d+(\.\d+)?)', sections[1])
        if match:
            item.armour = int(match.group(1))
        
        match = re.search(r'Energy Shield:\s*(\d+(\.\d+)?)', sections[1])
        if match:
            item.energy_shield = int(match.group(1))
        
        match = re.search(r'Attacks per Second:\s*(\d+(\.\d+)?)', sections[1])
        if match:
            item.attacks_per_second = float(match.group(1))

        match = re.search(r'Weapon Range:\s*(\d+(\.\d+)?)', sections[1])
        if match:
            item.weapon_range = float(match.group(1))

        match = re.search(r'Critical Strike Chance:\s*(\d+(\.\d+)?)', sections[1])
        if match:
            item.critical_strike_chance = float(match.group(1))

        match = re.search(r'Physical Damage:\s*(\d+)-(\d+)', sections[1])
        if match:
            item.physical_dmg["min"] = int(match.group(1))
            item.physical_dmg["max"] = int(match.group(2))

        # TODO: Elemental damage

        # Requirements
        match = re.search(r'Level:\s*(\d+(\.\d+)?)', sections[2])
        if match:
            item.requirements["level"] = int(match.group(1))

        match = re.search(r'Dex:\s*(\d+(\.\d+)?)', sections[2])
        if match:
            item.requirements["dex"] = int(match.group(1))

        match = re.search(r'Int:\s*(\d+(\.\d+)?)', sections[2])
        if match:
            item.requirements["int"] = int(match.group(1))

        match = re.search(r'Str:\s*(\d+(\.\d+)?)', sections[2])
        if match:
            item.requirements["str"] = int(match.group(1))

        # Sockets
        match = re.search(r"Sockets:\s*(.*)", sections[3])
        if match:
            item.sockets = "".join((match.group(1).replace("\n", "")).rsplit(" ", 1))

        links = (list(map(lambda x: len(x)-x.count("-"), item.sockets.split(" "))))
        links.sort(reverse=True)
        item.links = links[0]

        # Mods
        mods = []
        if("enchant" in sections[5]):

            if("implicit" in sections[6]):
                mods.extend(sections[7].splitlines())

            mods.extend(sections[6].splitlines())

        if("implicit" in sections[5]):
            mods.extend(sections[6].splitlines())

        mods.extend(sections[5].splitlines())
        item.mods = mods

        return item

from src.utils.parser import Parser

_FILES = ["./tests/parser/files/body_armour_rare_no_6l_6_20_shaper_&_elder_yes_multicraft_yes_no_poe.txt"]

if __name__ == "__main__":
    
    for file in _FILES:
        file = open(file, "r")
        text = file.read()
        
        item = Parser.parse(text)
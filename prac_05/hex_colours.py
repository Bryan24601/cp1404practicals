HEX_COLOUR_DICTIONARY = {"ABSOLUTEZERO":"#0048BA", "AMETHYST": "#9966CC", "AQUA": "#00FFFF",
                         "AUREOLIN": "#FDEE00", "BABYPINK": "#F4C2C2", "BITTERSWEETSHIMMER": "#BF4F51",
                         "BRASS": "#B5A642", "BYZANTIUM": "#702963", "CERULEANFROST": "#6D9B3C",
                         "COTTONCANDY": "#FFBCD9"}
print(HEX_COLOUR_DICTIONARY)

colour_name = input("Enter Colour Name: ").upper()
while colour_name != "":
    if colour_name in HEX_COLOUR_DICTIONARY:
        print(colour_name, "is", HEX_COLOUR_DICTIONARY[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter Colour Name: ").upper()

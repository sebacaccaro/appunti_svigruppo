from operator import itemgetter

alkaline_earth_metals = [56,4,20,12,88,38]


print("The highest atomic number is: ",max(alkaline_earth_metals))

alkaline_earth_metals.sort()
print("Sorted list is: ", alkaline_earth_metals)

alkaline_earth_metals = {
    56: "barium",
    4: "beryllium",
    20: "calcium",
    12: "magnesium",
    88: "radium",
    38: "strontium"
}
alkaline_earth_metals = {value:key for key, value in alkaline_earth_metals.items()}

noble_gases = {
    "helium": 56,
    "neon": 10,
    "argon": 18,
    "krypton": 36,
    "xenon": 54,
    "radon": 86
}

elements = {}
elements.update(noble_gases)
elements.update(alkaline_earth_metals)
elements_tuple = [(element,number) for element, number in elements.items()]
elements_tuple.sort(key=itemgetter(1))
print(elements_tuple)


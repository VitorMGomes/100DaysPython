# Key - Value

colours = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Pear": "Green",
    "Orange": "Yellow",
    "Blueberrry": "Blue",
}

print(colours["Apple"])
print("------------------------")

#same can be done to edit an item
colours["Strawberry"] = "Red"

print(colours)

print("------------------------")

empty_dictio = {}

print("------------------------")

for thing in colours:
    print(thing)
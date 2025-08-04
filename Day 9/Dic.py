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

# same can be done to edit an item
colours["Strawberry"] = "Red"

print(colours)

print("------------------------")

empty_dictionary = {}
# wipe an existing dictionary

print("------------------------")

for thing in colours:
    print(thing)
    
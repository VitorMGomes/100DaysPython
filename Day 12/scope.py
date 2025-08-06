enemies = 1
strengh = 10

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")


def increase_strength():
    global strengh
    strengh += 5
    print(f"Strength inside function: {strengh}")    
        
increase_enemies()
print(f"Enemies outside function: {enemies}")


print(f"Strength before potion: {strengh}")
increase_strength()
print(f"Strengt: {strengh}")


pato = None
print(pato)
pato = 5
print(pato)
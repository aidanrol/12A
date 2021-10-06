from random import randint

def roll():
    return randint(1, 6)

count = 0
dice = 0 
while dice != 6:
    dice = roll()
    count += 1
    print(f"You rolled a {dice}")

print(f"It took you {count} rolls to get a 6")


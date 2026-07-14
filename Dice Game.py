import random
from functools import total_ordering

# ● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "|         |"
# "|         |"
# "|         |"
# "└─────────┘"

dice_art={
    1:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘"),
    2:("┌─────────┐",
       "| ●       |",
       "|         |",
       "|       ● |",
       "└─────────┘"),
    3:("┌─────────┐",
       "| ●       |",
       "|    ●    |",
       "|       ● |",
       "└─────────┘"),
    4:("┌─────────┐",
       "| ●     ● |",
       "|         |",
       "| ●     ● |",
       "└─────────┘"),
    5:("┌─────────┐",
       "| ●     ● |",
       "|    ●    |",
       "| ●     ● |",
       "└─────────┘"),
    6:("┌─────────┐",
       "| ●     ● |",
       "| ●     ● |",
       "| ●     ● |",
       "└─────────┘")


}

dice=[]
total =0
num_of_dice=int(input("Enter the Number of Dice: "))
for i in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in range(num_of_dice):
    for shape in dice_art.get(dice[die]):
        print(shape)
    print(end=" ")

for die in dice:
    total+=die

print(f"The Total is {total}")

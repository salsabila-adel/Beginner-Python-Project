# Paper, Rock,and Scissors Game

import random
player=None

options=("rock","paper","scissors")
# player=None
player=input("Enter a choice (Rock,Paper,Scissors) or (q to quit) : ").lower()

while True:
    if player=='q':
        break
    else:
        computer=random.choice(options)
        while player not in options:
            player=input("Enter a available choice (Rock,Paper,Scissors) : ")


        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player==computer:
            print("It's a Tie")
        elif player=="rock" and computer=="scissors":
            print("You win")
        elif player=="scissors" and computer=="paper":
            print("You win")
        elif player=="paper" and computer=="rock":
            print("You win")
        else:
            print("you Lose")
    print("------------Happy Turn ☺️---------------")
    player = input("Enter a choice (Rock,Paper,Scissors) or (q to quit) : ").lower()

from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

player_1 = input("(enter player_1's choice): ")
# player_2 = input("(enter player_2's choice): ")
player_2 = None

random_digit = randint(0, 2)

if random_digit == 0:
    player_2 = "scissors"
elif random_digit == 1:
    player_2 = "paper"
else:
    player_2 = "rock"

print(f"The computer threw {player_2}")

if (player_1 == "rock" or player_1 == "scissors" or player_1 == "paper") and (player_2 == "rock" or player_2 == "scissors" or player_2 == "paper"):
    if player_1 == player_2:
        print("It's a tie.")
    elif (player_1 == "rock" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper") or (player_1 == "paper" and player_2 == "rock"):
        print("player_1 wins!")
    else:
        print("player_2 wins")
else:
    print("Someone tried to cheat.")

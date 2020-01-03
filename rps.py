
from random import randint


# player_2 = input("(enter player_2's choice): ")
p1_score = 0
comp_score = 0
winning_score = 3

while p1_score < winning_score and comp_score < winning_score:
    print(f"Player: {p1_score}, Computer: {comp_score}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    player_1 = input("(enter player_1's choice): ").lower()
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
            p1_score += 1
        else:
            print("The computer wins")
            comp_score += 1
    else:
        print("Someone tried to cheat.")

print(f"Player: {p1_score}, Computer: {comp_score}")
if p1_score > comp_score:
    print("HUMANS ARE THE BEST.")
else:
    print("MACHINES WILL RISE AGAINST US.")

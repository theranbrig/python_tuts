import random

random_number = random.randint(1, 10)
guess = None

while(guess != 10):
    guess = int(input("Guess a number between 1 and 10. "))
    if guess < random_number:
        print("Too low. Try again. ")
    elif(guess > random_number):
        print("Too high. Try again. ")
    else:
        print(f"That is correct.  The number was {random_number}.")
        keep_playing = input("Would you like to keep playing? (y/n):  ")
        if keep_playing == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thanks for playing")
            break

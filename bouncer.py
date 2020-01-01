print("How old are you?")
age = int(input())

# if age:
#     if age >= 21 and age < 21:
#         print("You can enter the club, but need a wristband.")
#     elif age > 21:
#         print("You can enter and drink.")
#     else:
#         print("You can not come in at all little one.")
# else:
#     print("Please enter an age!")


if age:
    if age >= 21:
        print("You can enter the club, and drink.")
    elif age >= 18:
        print("You can enter, but need a wristband.")
    else:
        print("You can not come in at all, little one.")
else:
    print("Please enter an age!")

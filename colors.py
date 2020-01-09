from termcolor import colored
from pyfiglet import figlet_format as format

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

  
def print_art(msg, color):
    if color not in valid_colors:
        color = "cyan"
    ascii_art = colored(format(phrase), color=color)
    print(ascii_art)


phrase = input("What would you like this to say? ")
color = input("What color would you like this to print in? ")
print_art(phrase, color)

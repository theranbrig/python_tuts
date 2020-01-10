import requests
from termcolor import colored
from pyfiglet import figlet_format as format
import random

# url = 'http://www.google.com'
# res = requests.get(url)

# print(f"Request: {url}, Status Code: {res.status_code}")
print(colored(format("DAD JOKE 3000"), color="cyan"))

search = input("What kind of joke would you like? ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url, headers={"Accept": "application/json"}, params={"term": search})

data = res.json()

number_of_jokes = len(data["results"])

def print_joke():
  if number_of_jokes == 0:
      print("Sorry.  No jokes found")
  elif number_of_jokes == 1:
      print(f"I've got one joke about {search}.  Here it is:")
      print(data["results"][0]["joke"])
  else:
      joke = random.choice(data["results"])
      print(f"I've got {number_of_jokes} jokes about {search}.  Here is one.")
      print(joke["joke"])

print_joke()

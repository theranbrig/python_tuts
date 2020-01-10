import requests
from termcolor import colored
from pyfiglet import figlet_format as format

# url = 'http://www.google.com'
# res = requests.get(url)

# print(f"Request: {url}, Status Code: {res.status_code}")
print(colored(format("DAD JOKE 3000"), color="cyan"))

search = input("What kind of joke would you like? ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url, headers={"Accept": "application/json"}, params={"term": search})

data = res.json()

joke_count = 0
if len(data["results"]) == 0:
    print("Sorry.  No jokes found")
else:
    for item in data["results"]:
        joke_count += 1
        print(f"JOKE {joke_count}")
        print(item["joke"])

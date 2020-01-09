import requests

# url = 'http://www.google.com'
# res = requests.get(url)

# print(f"Request: {url}, Status Code: {res.status_code}")

url = "https://icanhazdadjoke.com/"

res = requests.get(url, headers={"Accept": "application/json"})

data = res.json()

print(res.text)
print(data["joke"])

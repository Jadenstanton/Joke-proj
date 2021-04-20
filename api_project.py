import requests
from random import choice
import pyfiglet

header = pyfiglet.figlet_format("Dad jokes")
print(header)
term = input("what would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term":term}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {term}. heres one: ")
    print(choice(results)['joke'])
elif num_jokes == 1:
    print("there is one joke")
    print(results[0]['joke'])
else:
    print(f"soory, theres no jokes for {term}")
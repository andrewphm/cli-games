# import the json module from python3
import json

# open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

for item in data["cards"]:
    guess = input(item["q"] + " > ")
    
    if guess == item["a"]:
        print("Correct!")
    else:
        print(f'Inccorect! The correct answer was {item["a"]}.')


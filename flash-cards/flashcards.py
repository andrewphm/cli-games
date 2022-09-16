# import the json module from python3
import json

# open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0

for item in data["cards"]:
    guess = input(item["q"] + " > ")
    
    if guess.lower() == item["a"].lower():
        score += 1
        print(f"Correct! Current score: {score}/{total}")
    else:
        print(f'Inccorect! The correct answer was {item["a"]}.')
        print(f"Correct! Current score: {score}/{total}")

end_game_message = f"Thanks for playing! You scored: {score} out of {total} correct!"

print(end_game_message)

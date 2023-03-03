import requests

# Send HTTP get request to deckofcardsapi and place response in variable
response = requests.get('https://deckofcardsapi.com/api/deck/new/')

# If HTTP request successful, shuffle deck of cards. If no, exit program
if response.status_code == 200:
    deck_id = response.json()['deck_id']
    requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/")
else:
    print(f"Request unsuccessful. Status code: {response.status_code}")
    exit()
    
# send another HTTP request to get 5 cards from you deck of cards nd place in JSON obj
draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")
draw = draw_response.json()

from pprint import pprint
pprint(draw)

# Loop through JSON object and print each card value
i = 1

for card in draw['cards']:
    print(f"Card {i} is {card['value']} of {card['suit']}")
    i +=1
    
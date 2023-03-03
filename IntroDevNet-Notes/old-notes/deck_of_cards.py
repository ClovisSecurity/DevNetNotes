{\rtf1\ansi\ansicpg1252\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
{\info
{\author John Moorman}}\margl1440\margr1440\vieww28300\viewh17140\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
\
# Send HTTP get request to deckofcardsapi and place response in variable\
response = requests.get('https://deckofcardsapi.com/api/deck/new/')\
\
# If HTTP request successful, shuffle deck of cards. If no, exit program\
if response.status_code == 200:\
    deck_id = response.json()['deck_id']\
    requests.get(f"https://deckofcardsapi.com/api/deck/\{deck_id\}/shuffle/")\
else:\
    print(f"Request unsuccessful. Status code: \{response.status_code\}")\
    exit()\
    \
# send another HTTP request to get 5 cards from you deck of cards nd place in JSON obj\
draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/\{deck_id\}/draw/?count=5")\
draw = draw_response.json()\
\
from pprint import pprint\
pprint(draw)\
\
# Loop through JSON object and print each card value\
i = 1\
\
for card in draw['cards']:\
    print(f"Card \{i\} is \{card['value']\} of \{card['suit']\}")\
    i +=1\
    }
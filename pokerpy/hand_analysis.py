import json
import re

fn = r"""/home/jon/data/poker/3024637274"""

with open(fn, 'r') as f:
    #data = f.read()

    lines = f.readlines()

current_hand = None
hands = {}

sections = ('HOLE CARDS',
            'FLOP',
            'TURN',
            'RIVER',
            'SHOW DOWN',
            'SUMMARY',
            )

for line in lines:
    is_new_hand = line.startswith('***********')
    if is_new_hand:
        if current_hand:
            hands[hand] = current_hand

        current_hand = {
            'START': [],
            'HOLE CARDS': [],
            'FLOP': [],
            'TURN': [],
            'RIVER': [],
            'SHOW DOWN': [],
            'SUMMARY': [],
        }
        current_section = 'START'
        hand = int(re.search(r'(\d+)', line).groups(1)[0])
        print(hand)

    else:

        for section in sections:
            header = f'*** {section} ***'
            if line.startswith(header):
                current_section = section

        current_hand[current_section].append(line.strip())

#print(hands[1])

print(json.dumps(hands[1], indent=4))
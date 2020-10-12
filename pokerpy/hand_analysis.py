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

first_in_raise = {}

def get_player(line):
    player_search = re.search('Seat (\d): (\w*)', line)
    if player_search:
        return player_search.groups()

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
            'PLAYERS':{}
        }
        current_section = 'START'
        hand = int(re.search(r'(\d+)', line).groups(1)[0])
        print(hand)

    else:

        for section in sections:
            header = f'*** {section} ***'
            if line.startswith(header):
                current_section = section

                unraised = True
                uncalled = True

        current_hand[current_section].append(line.strip())

        if current_section=='START':
            ply = get_player(line)
            if ply:
                player_seat, player_name = ply
                current_hand['PLAYERS'][player_seat] = player_name

        elif current_section in {'HOLE CARDS'}:
            if 'raises' in  line:
                player = line.split(':')[0]
                print(player, 'raises')

                if unraised and uncalled:
                    first_in_raise[player] = first_in_raise.get(player_name, 0)
                    first_in_raise[player] +=1

                unraised=False
            elif ' calls ' in line:
                uncalled = False

#print(hands[1])

print(json.dumps(hands[1], indent=4))

print(first_in_raise)
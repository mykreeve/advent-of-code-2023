import copy
from itertools import product

file = open('./input/day7input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

hands = []

for line in file:
    line = line.split(' ')
    hand = line[0]
    bid = int(line[1])
    hands.append({'hand': hand, 'bid': bid})

CARD_VALUES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

VICTORIES = ['5oak', '4oak', 'fh', '3oak', '2p', '1p', 'high']


def hand_assessment(hand):
    breakdown = {}
    for card in hand:
        if card not in breakdown:
            breakdown[card] = 1
        else:
            breakdown[card] += 1
    breakdown = (list(breakdown.values()))
    breakdown.sort(reverse=True)
    if breakdown[0] == 5:
        return '5oak'
    if breakdown[0] == 4:
        return '4oak'
    if breakdown[0] == 3 and breakdown[1] == 2:
        return 'fh'
    if breakdown[0] == 3:
        return '3oak'
    if breakdown[0] == 2 and breakdown[1] == 2:
        return '2p'
    if breakdown[0] == 2:
        return '1p'
    return 'high'


def compare(first, second, comparison_field):
    first_score = VICTORIES.index(first[comparison_field])
    second_score = VICTORIES.index(second[comparison_field])
    if (first_score < second_score):
        return 'first'
    if (first_score > second_score):
        return 'second'
    for pos in range(len(first['hand'])):
        if CARD_VALUES.index(first['hand'][pos]) < CARD_VALUES.index(second['hand'][pos]):
            return 'first'
        if CARD_VALUES.index(first['hand'][pos]) > CARD_VALUES.index(second['hand'][pos]):
            return 'second'


new_hands = []
for item in hands:
    item = {'hand': item['hand'], 'bid': item['bid'],
            'assess': hand_assessment(item['hand'])}
    new_hands.append(item)
hands = copy.deepcopy(new_hands)

swaps = None
while swaps != 0:
    new_hands = []
    swaps = 0
    while len(hands) > 1:
        first = hands.pop(0)
        second = hands.pop(0)
        winner = compare(first, second, 'assess')
        # put winner into new_hands, loser back into hands
        if winner == 'first':
            new_hands.append(first)
            hands.insert(0, second)
        if winner == 'second':
            swaps += 1
            new_hands.append(second)
            hands.insert(0, first)
    new_hands.append(hands[0])
    hands = copy.deepcopy(new_hands)
tot = 0
hands.reverse()

# print(hands[0], hands[1])

for i, h in enumerate(hands):
    # print(i, h)
    tot = tot + (h['bid'] * (i+1))

print('Answer to part 1:', tot)

CARD_VALUES = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

perm1 = list(product(CARD_VALUES))
perm2 = list(product(CARD_VALUES, CARD_VALUES))
perm3 = list(product(CARD_VALUES, CARD_VALUES, CARD_VALUES))

PERM_LOOKUP = [[], perm1, perm2, perm3]


def get_possibles(hand):
    if 'J' not in hand:
        return [hand]
    hand = [*hand]
    possibles = []
    positions = []
    for pos in range(len(hand)):
        if hand[pos] == 'J':
            positions.append(pos)
    # print(hand, len(positions))
    if (len(positions) == 4):
        for pos in range(len(hand)):
            if hand[pos] != 'J':
                ret = ''.join(
                    [hand[pos], hand[pos], hand[pos], hand[pos], hand[pos]])
                return [ret]
    if (len(positions) == 5):
        return [hand]
    perm = PERM_LOOKUP[len(positions)]
    for p in perm:
        for index, pos in enumerate(positions):
            hand[pos] = p[index]
            if (''.join(hand) not in possibles):
                possibles.append(''.join(hand))
    return possibles


# print('Generating alternates')
new_hands = []
for item in hands:
    item = {'hand': item['hand'], 'bid': item['bid'],
            'assess': item['assess'], 'alterns': get_possibles(item['hand'])}
    new_hands.append(item)
hands = copy.deepcopy(new_hands)
# print('Got alternates')


def get_best_assess(alts):
    outcomes = []
    for a in alts:
        outcomes.append(VICTORIES.index(hand_assessment(a)))
    return min(outcomes)


# print('Assessing alternates')
new_hands = []
for item in hands:
    item = {'hand': item['hand'], 'bid': item['bid'],
            'assess': item['assess'], 'alterns': item['alterns'], 'alt_assess': VICTORIES[get_best_assess(item['alterns'])]}
    new_hands.append(item)
hands = copy.deepcopy(new_hands)
# print('Finished assessing alternates')


swaps = None
while swaps != 0:
    new_hands = []
    swaps = 0
    while len(hands) > 1:
        first = hands.pop(0)
        second = hands.pop(0)
        winner = compare(first, second, 'alt_assess')
        # put winner into new_hands, loser back into hands
        if winner == 'first':
            new_hands.append(first)
            hands.insert(0, second)
        if winner == 'second':
            swaps += 1
            new_hands.append(second)
            hands.insert(0, first)
    new_hands.append(hands[0])
    hands = copy.deepcopy(new_hands)
    # print(swaps)

tot = 0
hands.reverse()

# print(hands[0], hands[1])

for i, h in enumerate(hands):
    # print(i, h)
    tot = tot + (h['bid'] * (i+1))

print('Answer to part 2:', tot)

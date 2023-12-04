file = open('./input/day4input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

cards = []

for line in file:
    line = line.split(' |')
    line_part = line[0].split(': ')
    line_number = int(line_part[0].replace(' ', '').replace('Card', ''))
    winners = line_part[1].replace('  ', ' ').strip().split(' ')
    winners = list(map(lambda x: int(x), winners))
    numbers = line[1].replace('  ', ' ').strip().split(' ')
    numbers = list(map(lambda x: int(x), numbers))
    cards.append((line_number, winners, numbers))

new_cards = []
tot = 0
for (line, winners, numbers) in cards:
    score = 0
    match = 0
    for w in winners:
        if w in numbers:
            match += 1
            if score == 0:
                score = 1
            else:
                score = score * 2
    tot += score
    new_cards.append((line, match))


print('Answer for part 1:', tot)

freq = []
for c in new_cards:
    freq.append(1)
for (line, match) in new_cards:
    for iter in range(match):
        freq[line+iter] = freq[line+iter] + (freq[line - 1])

tot = 0
for n in freq:
    tot += n

print('Answer for part 2:', tot)

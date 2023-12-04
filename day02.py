file = open('./input/day2input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))


def is_number(x):
    return x in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def process_game(string):
    string = string.split(': ')
    game_number = int(string[0].replace('Game ', ''))
    draws = string[1].split('; ')
    sorted = []
    for f in draws:
        pos = 0
        draw = {}
        number = ''
        colour = ''
        while pos < len(f):
            if is_number(f[pos]):
                number += f[pos]
                pos += 1
            elif f[pos] == ' ':
                pos += 1
            elif f[pos] == ',':
                pos += 2
                draw[colour] = int(number)
                colour = ''
                number = ''
            else:
                colour += f[pos]
                pos += 1
        draw[colour] = int(number)
        colour = ''
        number = ''
        sorted.append(draw)
    return (game_number, sorted)


tot = 0

for f in file:
    (number, draws) = process_game(f)
    valid = True
    for d in draws:
        if 'red' in d and d['red'] > 12:
            valid = False
        if 'green' in d and d['green'] > 13:
            valid = False
        if 'blue' in d and d['blue'] > 14:
            valid = False
    if valid:
        tot += number

print('Answer to part 1:', tot)

tot = 0
for f in file:
    (number, draws) = process_game(f)
    red = 0
    green = 0
    blue = 0
    for d in draws:
        if 'red' in d and d['red'] > red:
            red = d['red']
        if 'green' in d and d['green'] > green:
            green = d['green']
        if 'blue' in d and d['blue'] > blue:
            blue = d['blue']
    power = red * green * blue
    tot += power


print('Answer to part 2:', tot)

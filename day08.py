import copy
import math

file = open('./input/day8input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

instructions = [*file[0]]

directions = {}
for i in range(2, len(file)):
    i = file[i].split(' = ')
    # print(tuple(i[1].replace('(', '').replace(')', '').replace(' ', '').split(',')))
    directions[i[0]] = tuple(i[1].replace(
        '(', '').replace(')', '').replace(' ', '').split(','))

loc = 'AAA'
steps = 0
while loc != 'ZZZ':
    steps += 1
    current = instructions.pop(0)
    if current == 'L':
        loc = directions[loc][0]
    elif current == 'R':
        loc = directions[loc][1]
    instructions.append(current)
    # print(steps, current, loc)

print('Answer to part 1:', steps)


def all_vals_populated(array):
    for a in array:
        if a == None:
            return False
    return True


loc = []
for i in directions:
    if i[-1] == 'A':
        loc.append(i)
steps = 0
freqs = [None, None, None, None, None, None]
while all_vals_populated(freqs) == False:
    steps += 1
    current = instructions.pop(0)
    new_loc = []
    if current == 'L':
        for l in loc:
            new_loc.append(directions[l][0])
    elif current == 'R':
        for l in loc:
            new_loc.append(directions[l][1])
    loc = copy.deepcopy(new_loc)
    instructions.append(current)
    if loc[0][-1] == 'Z':
        freqs[0] = steps
    if loc[1][-1] == 'Z':
        freqs[1] = steps
    if loc[2][-1] == 'Z':
        freqs[2] = steps
    if loc[3][-1] == 'Z':
        freqs[3] = steps
    if loc[4][-1] == 'Z':
        freqs[4] = steps
    if loc[5][-1] == 'Z':
        freqs[5] = steps

print('Answer to part 2:', math.lcm(*freqs))

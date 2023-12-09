import copy
from itertools import groupby


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


file = open('./input/day9input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', '').split(' '), file))

tot = 0
for thing in file:
    thing = list(map(lambda x: int(x), thing))
    analysis = [thing]
    while not all_equal(thing):
        new_thing = []
        for a in range(len(thing) - 1):
            new_thing.append(thing[a+1] - thing[a])
        analysis.append(new_thing)
        thing = copy.deepcopy(new_thing)
    analysis.reverse()
    analysis[0].append(analysis[0][0])
    for a in range(len(analysis) - 1):
        analysis[a+1].append(analysis[a+1][len(analysis[a+1])-1] +
                             analysis[a][len(analysis[a]) - 1])
    tot += analysis[len(analysis) - 1][len(analysis[len(analysis) - 1]) - 1]

print('Answer to part 1:', tot)

tot = 0
for thing in file:
    thing = list(map(lambda x: int(x), thing))
    analysis = [thing]
    while not all_equal(thing):
        new_thing = []
        for a in range(len(thing) - 1):
            new_thing.append(thing[a+1] - thing[a])
        analysis.append(new_thing)
        thing = copy.deepcopy(new_thing)
    analysis.reverse()
    analysis[0].append(analysis[0][0])
    for a in range(len(analysis) - 1):
        analysis[a+1].insert(0, analysis[a+1][0] - analysis[a][0])
    tot += analysis[len(analysis) - 1][0]

print('Answer to part 2:', tot)

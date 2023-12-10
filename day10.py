import copy

file = open('./input/day10input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

grid = {}

for y, line in enumerate(file):
    for x, ch in enumerate(line):
        grid[(x, y)] = ch
        if ch == 'S':
            start = (x, y)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

# north, east, south, west
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# these tiles accept from these directions
connections = {'|': [(0, 1), (0, -1)],
               '-': [(1, 0), (-1, 0)],
               'L': [(0, 1), (-1, 0)],
               'J': [(0, 1), (1, 0)],
               '7': [(0, -1), (1, 0)],
               'F': [(0, -1), (-1, 0)],
               '.': []
               }

# evaluate start
dirs_from_start = []
for d in directions:
    test = (start[0]+d[0], start[1]+d[1])
    if d in connections[grid[test]]:
        dirs_from_start.append((-d[0], -d[1]))
for c in connections:
    count = 0
    for d in dirs_from_start:
        if d in connections[c]:
            count += 1
    if count == 2:
        grid[start] = c

# for y in range(start[1]-2, start[1]+3):
#     for x in range(start[0]-2, start[0]+3):
#         print(grid[(x, y)], end='')
#     print()

journey = [start]
loc = copy.deepcopy(start)
while loc != start or len(journey) < 2:
    # print('current_tile:', loc, grid[loc])
    for d in directions:
        if (-d[0], -d[1]) in connections[grid[loc]]:
            test = (loc[0]+d[0], loc[1]+d[1])
            if test in grid and d in connections[grid[test]] and (test not in journey or (test == start and len(journey) > 2)):
                # print(loc, test)
                journey.append(test)
                loc = copy.deepcopy(test)
                break

journey.pop(len(journey) - 1)

print('Answer to part 1:', int(len(journey)) / 2)

for g in grid:
    if g not in journey:
        grid[g] = '.'

# Using the non-zero rule - https://en.wikipedia.org/wiki/Nonzero-rule
count = 0
for y in range(len(file)-1):
    score = 0
    for x in range(len(line)):
        if grid[(x, y)] == '.' and score != 0:
            grid[(x, y)] = '*'
            count += 1
        elif grid[(x, y)] != '.':
            journeypos = journey.index((x, y))
            prevpos = (journeypos - 1) % len(journey)
            nextpos = (journeypos + 1) % len(journey)

            if journey[prevpos] == (x, y-1):
                score += 1
            if journey[nextpos] == (x, y-1):
                score -= 1

print('Answer to part 2:', count)

# for y in range(0, 140):
#     for x in range(0, 140):
#         if grid[(x, y)] == '*':
#             print(f'\033[92m{grid[(x,y)]}', end='')
#         else:
#             print(f'\033[0m{grid[(x, y)]}', end='')
#     print()

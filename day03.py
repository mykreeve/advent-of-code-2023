file = open('./input/day3input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

grid = {}
for y, row in enumerate(file):
    for x, item in enumerate(row):
        grid[(x, y)] = item

xpos = 0
ypos = 0
numbers_found = []
while ypos < len(file):
    while xpos < len(row):
        if grid[(xpos, ypos)] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            xpos += 1
            continue
        start_loc = (xpos, ypos)
        number = grid[(xpos, ypos)]
        while (xpos + 1, y) in grid and grid[(xpos + 1, ypos)] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            number += grid[(xpos + 1, ypos)]
            xpos += 1
        xpos += 1
        numbers_found.append((start_loc, number))
    ypos += 1
    xpos = 0

tot = 0
for n in numbers_found:
    start_loc = n[0]
    number = n[1]
    valid = False
    for ypos in range(start_loc[1]-1, start_loc[1] + 2):
        for xpos in range(start_loc[0]-1, start_loc[0] + len(number) + 1):
            if (xpos, ypos) in grid and grid[(xpos, ypos)] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                # print((xpos, ypos), grid[(xpos, ypos)])
                valid = True
    # print(start_loc, number, valid)
    if valid:
        tot += int(number)

print('Answer for part 1:', tot)

num_lookup = {}
for n in numbers_found:
    num_lookup[n[0]] = int(n[1])

gears_found = []
xpos = 0
ypos = 0
while ypos < len(file):
    while xpos < len(row):
        if grid[(xpos, ypos)] != '*':
            xpos += 1
            continue
        gears_found.append((xpos, ypos))
        xpos += 1
    ypos += 1
    xpos = 0

valid_gears = []

for g in gears_found:
    # print(g)
    surrounds = []
    for ypos in range(g[1]-1, g[1]+2):
        for xpos in range(g[0]-1, g[0] + 2):
            if grid[(xpos, ypos)] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                xfinder = xpos
                num_found = None
                while not num_found:
                    if (xfinder, ypos) in num_lookup:
                        num_found = (xfinder, ypos)
                    xfinder -= 1
                if num_found not in surrounds:
                    surrounds.append(num_found)
    if len(surrounds) == 2:
        valid_gears.append(surrounds)

tot = 0
for v in valid_gears:
    tot += num_lookup[v[0]] * num_lookup[v[1]]

print('Answer to part 2:', tot)

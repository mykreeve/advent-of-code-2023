import copy
file = open('./input/day14input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

grid = {}
for y, line in enumerate(file):
    for x in range(len(line)):
        grid[(x, y)] = line[x]


def get_direction(pos, string):
    if string == 'north':
        return (pos[0], pos[1]-1)
    if string == 'east':
        return (pos[0]+1, pos[1])
    if string == 'south':
        return (pos[0], pos[1]+1)
    if string == 'west':
        return (pos[0]-1, pos[1])


def determine_load(grid):
    score = 0
    for g in grid:
        if grid[g] == 'O':
            score += rows - g[1]
    return score


def do_movement(grid, direction):
    moves = 999
    while moves != 0:
        moves = 0
        new_grid = copy.deepcopy(grid)
        for g in grid:
            move = get_direction(g, direction)
            if move in grid and new_grid[g] == 'O' and new_grid[move] == '.':
                new_grid[move] = 'O'
                new_grid[g] = '.'
                moves += 1
        grid = copy.deepcopy(new_grid)
    # print(f'Completed move {direction}')
    return grid


rows = len(file)
cols = len(line)

grid = do_movement(grid, 'north')
score = determine_load(grid)

print('Answer to part 1:', score)

# Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east.
grid = do_movement(grid, 'west')
grid = do_movement(grid, 'south')
grid = do_movement(grid, 'east')


def do_cycle(grid):
    grid = do_movement(grid, 'north')
    grid = do_movement(grid, 'west')
    grid = do_movement(grid, 'south')
    grid = do_movement(grid, 'east')
    return grid


cycle_scores = [determine_load(grid)]
completed_cycles = 1

cycle_not_found = True
while cycle_not_found:
    grid = do_cycle(grid)
    completed_cycles += 1
    score = determine_load(grid)
    print(f'Completed cycle {completed_cycles} - score: {score}')
    cycle_scores.append(score)

    if len(cycle_scores) > 120:
        last_ten = cycle_scores[-10:]
        for x in range(len(cycle_scores) - 20):
            if cycle_scores[x:x+10] == last_ten:
                start = x + 1
                end = len(cycle_scores) - 10 + 1
                cycle_not_found = False

print("Repetition detected")

cycle_length = end - start
reqd_cycles = 1000000000 - start
diff = reqd_cycles % cycle_length
pos = start + diff
print(cycle_scores[pos - 1])

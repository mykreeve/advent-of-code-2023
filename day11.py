from itertools import combinations

file = open('./input/day11input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

dupe_rows = []

for line in file:
    if '#' not in line:
        dupe_rows.append(line)
    dupe_rows.append(line)

# print(len(dupe_rows))

dupe_columns = []

for x in range(len(line)):
    m = list(map(lambda r: r[x], dupe_rows))
    if '#' not in m:
        dupe_columns.append(x)

expanded = []
for d in dupe_rows:
    expanded_row = ''
    for i, ch in enumerate(d):
        if i in dupe_columns:
            expanded_row += ch
        expanded_row += ch
    expanded.append(expanded_row)

grid = {}

for y, line in enumerate(expanded):
    for x, ch in enumerate(line):
        grid[(x, y)] = ch

# for y in range(len(expanded)):
#     for x in range(len(line)):
#         print(f'\033[0m{grid[(x, y)]}', end='')
#     print()

galaxies = []
for g in grid:
    if grid[g] == '#':
        galaxies.append(g)

tot = 0
pairs = list(combinations(galaxies, 2))
for p in pairs:
    dist = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])
    tot += dist
print('Answer to part 1:', tot)

EXPANSION_SIZE = 1000000

grid = {}

for y, line in enumerate(file):
    for x, ch in enumerate(line):
        grid[(x, y)] = ch

dupe_rows = []
for index, line in enumerate(file):
    if '#' not in line:
        dupe_rows.append(index)

galaxies = []
for g in grid:
    if grid[g] == '#':
        galaxies.append(g)
pairs = list(combinations(galaxies, 2))

tot = 0
for p in pairs:
    columns_involved = [p[0][0], p[1][0]]
    columns_involved.sort()
    column_journey = columns_involved[1] - columns_involved[0]
    columns_traversed = range(columns_involved[0], columns_involved[1])
    for c in columns_traversed:
        if c in dupe_columns:
            column_journey += (EXPANSION_SIZE - 1)
    rows_involved = [p[0][1], p[1][1]]
    rows_involved.sort()
    row_journey = rows_involved[1] - rows_involved[0]
    rows_traversed = range(rows_involved[0], rows_involved[1])
    for r in rows_traversed:
        if r in dupe_rows:
            row_journey += (EXPANSION_SIZE - 1)
    tot += (row_journey + column_journey)

print('Answer to part 2:', tot)

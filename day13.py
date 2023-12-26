import copy
file = open('./input/day13input.txt')


def assess_field(field, symCheck=None, posCheck=None):
    # print(field)
    similars = {}
    for i, line in enumerate(field):
        pos = None
        try:
            pos = field.index(line, i+1)
        except ValueError:
            pos = None
        if pos:
            similars[i] = pos
    m = list(similars.keys())
    m.sort()
    m.reverse()
    for s in m:
        # print(s, similars)
        if s+1 == similars[s]:
            # print('Possible horizontal midpoint')
            max_sims = min(s, (len(field)-1) - (s+1))
            valid = True
            for test in range(s-max_sims, s):
                if test not in similars:
                    valid = False
            if valid:
                # print(f'Appears valid horizontal midpoint at {s+1}')
                if (symCheck != 'horiz' or (posCheck != s+1 and posCheck != s+2)):
                    # input('.')
                    return ('horiz', s+1)
    rotate = [*field[0]]
    for l in range(1, len(field)):
        for ix, c in enumerate(field[l]):
            rotate[ix] = rotate[ix] + c
    similars = {}
    for i, line in enumerate(rotate):
        pos = None
        try:
            pos = rotate.index(line, i+1)
        except ValueError:
            pos = None
        if pos:
            similars[i] = pos
    m = list(similars.keys())
    m.sort()
    # print(m)
    for s in m:
        # print(s, similars)
        if s+1 == similars[s]:
            # print(f'Possible vertical midpoint at {s+1}')
            max_sims = min(s, (len(rotate)-1) - (s+1))
            # print(max_sims)
            valid = True
            for test in range(abs(s-max_sims), s):
                # print(test)
                if test not in similars:
                    valid = False
                # print(test, s, test+(2*(s-test))+1, rotate[test])
                if rotate[test] != rotate[test+(2*(s-test))+1]:
                    valid = False
            # print(test, valid)
            if valid:
                # print(f'Appears valid vertical midpoint at {s+1}')
                if (symCheck != 'vert' or (posCheck != s+1 and posCheck != s+2)):
                    return ('vert', s+1)
    return ('none', None)


def print_field(field, sym, pos):
    print(sym, pos)
    for i, f in enumerate(field):
        if sym == 'horiz' and i == pos:
            print('')
        if sym == 'vert':
            print(f[:pos], f[pos:])
        else:
            print(f)


vals = []
puzzles = file.read().split('\n\n')
for p in puzzles:
    puz = p.split('\n')
    (sym, pos) = assess_field(puz)
    vals.append((sym, pos))


score = 0
for (sym, pos) in vals:
    if (sym == 'horiz'):
        score += 100 * pos
    elif (sym == 'vert'):
        score += pos

print('Answer to part 1:', score)


def do_complex_thing(puz):
    (sym, pos) = assess_field(puz)
    for x in range(len(puz)):
        for y in range(len(puz[0])):
            changed = copy.deepcopy(puz)
            if changed[x][y] == '.':
                changed[x] = changed[x][:y] + '#' + changed[x][(y+1):]
            elif changed[x][y] == '#':
                changed[x] = changed[x][:y] + '.' + changed[x][(y+1):]
            (s, p) = assess_field(changed, sym, pos)
            if s and p:
                return (s, p)


vals = []
for p in puzzles:
    puz = p.split('\n')
    x = do_complex_thing(puz)
    vals.append(x)


score = 0
for (sym, pos) in vals:
    if (sym == 'horiz'):
        score += 100 * pos
    elif (sym == 'vert'):
        score += pos

print('Answer to part 2:', score)

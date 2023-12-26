from itertools import combinations
from functools import cache
import copy

file = open('./input/day12input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))


@cache
def num_valid_solutions(record, groups):
    if not record:
        return len(groups) == 0

    if not groups:
        return "#" not in record

    char, rest_of_record = record[0], record[1:]

    if char == ".":
        return num_valid_solutions(rest_of_record, groups)

    if char == "#":
        group = groups[0]
        if (
            len(record) >= group
            and all(c != "." for c in record[:group])
            and (len(record) == group or record[group] != "#")
        ):
            return num_valid_solutions(record[group + 1:], groups[1:])

        return 0

    if char == "?":
        return num_valid_solutions(f"#{rest_of_record}", groups) + num_valid_solutions(
            f".{rest_of_record}", groups
        )


def assess_springs(springs, target):
    assess = []
    current_run = 0
    for s in springs:
        if s == '.':
            if current_run > 0:
                assess.append(current_run)
                if assess != target[0:len(assess)]:
                    return False
            current_run = 0
        if s == '#':
            current_run += 1
    if current_run > 0:
        assess.append(current_run)
    if assess == target:
        return True
    return False


def question_marks(string):
    objs = []
    for index, s in enumerate(string):
        if s == '?':
            objs.append(index)
    return objs


def already_present(string):
    c = 0
    for s in string:
        if s == '#':
            c += 1
    return c


def get_options(string, target):
    already = already_present(string)
    expected = sum(target)
    options = question_marks(string)
    required = expected - already
    options = list(combinations(options, required))
    template = string.replace('?', '.')
    output = []
    for o in options:
        working = copy.deepcopy([*template])
        for i in o:
            working[i] = '#'
        output.append(''.join(working))
    return output


good = 0

for f in file:
    f = f.split(' ')
    springs = f[0]
    target = f[1].split(',')
    target = list(map(lambda x: int(x), target))
    options = get_options(springs, target)
    for o in options:
        if assess_springs(o, target):
            good += 1

print('Answer to part 1:', good)

good = 0
for f in file:
    f = f.split(' ')
    springs = f[0]+'?'+f[0]+'?'+f[0]+'?'+f[0]+'?'+f[0]
    target = f[1]+','+f[1]+','+f[1]+','+f[1]+','+f[1]
    target = target.split(',')
    target = list(map(lambda x: int(x), target))
    good += num_valid_solutions(springs, tuple(target))
    input('.')

print('Answer to part 2:', good)

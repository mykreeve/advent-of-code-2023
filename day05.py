import copy

file = open('./input/day5input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

mconverters = []
converters = []
converter = {}

for line in file:
    if 'seeds' in line:
        line = line.replace('seeds: ', '').split(' ')
        seeds = list(map(lambda x: int(x), line))
    elif 'map' in line:
        if len(converters) > 0:
            mconverters.append(converters)
            converters = []
        converter = {}
    elif line != '':
        line = line.split(' ')
        line = list(map(lambda x: int(x), line))
        start = line[1]
        end = line[1] + line[2] - 1
        convert = line[0] - line[1]
        converter = {'start': start, 'end': end, 'convert': convert}
        converters.append(converter)
mconverters.append(converters)


def get_output(val):
    for i, m in enumerate(mconverters):
        new_value = copy.deepcopy(val)
        for c in m:
            if val >= c['start'] and val <= c['end']:
                new_value = val + c['convert']
                # print(i, c, new_value)
        val = copy.deepcopy(new_value)
        # print('-==--', val)
        # input('.')
    return val


def get_outputs(seeds):
    outputs = []
    for seed in seeds:
        # print('---', seed)
        seed = get_output(seed)
        outputs.append(seed)
    return outputs


outputs = get_outputs(seeds)

print('Answer to part 1:', min(outputs))

seed_ranges = []
for i, s in enumerate(seeds):
    if i % 2 == 1:
        seed_range = {'start': seeds[i-1], 'end': seeds[i-1]+s}
        seed_ranges.append(seed_range)

new_ranges = copy.deepcopy(seed_ranges)
for mi, m in enumerate(mconverters):
    current_ranges = copy.deepcopy(new_ranges)
    new_ranges = []
    for seed_range in current_ranges:
        overlaps = []
        for i, c in enumerate(m):
            if seed_range['start'] >= c['start'] and seed_range['start'] <= c['end'] and seed_range['end'] <= c['end'] and seed_range['end'] >= c['start']:
                overlaps.append(c)
            if seed_range['start'] >= c['start'] and seed_range['start'] <= c['end'] and c not in overlaps:
                overlaps.append(c)
            if seed_range['end'] <= c['end'] and seed_range['end'] >= c['start'] and c not in overlaps:
                overlaps.append(c)
        if len(overlaps) > 0:
            sorted_overlaps = sorted(overlaps, key=lambda x: (x['start']))
            for o in sorted_overlaps:
                if o['start'] == seed_range['start']:
                    if o['end'] >= seed_range['end']:
                        new_ranges.append(
                            {'start': seed_range['start'] + o['convert'], 'end': seed_range['end'] + o['convert']})
                        seed_range = None
                    elif o['end'] < seed_range['end']:
                        new_ranges.append(
                            {'start': seed_range['start'] + o['convert'], 'end': o['end'] + o['convert']})
                        seed_range = {
                            'start': o['end'] + 1, 'end': seed_range['end']}
                elif o['start'] < seed_range['start']:
                    if o['end'] >= seed_range['end']:
                        new_ranges.append(
                            {'start': seed_range['start'] + o['convert'], 'end': seed_range['end'] + o['convert']})
                        seed_range = None
                    elif o['end'] < seed_range['end']:
                        new_ranges.append(
                            {'start': seed_range['start'] + o['convert'], 'end': o['end'] + o['convert']})
                        seed_range = {
                            'start': o['end'] + 1, 'end': seed_range['end']}
                elif o['start'] > seed_range['start']:
                    new_ranges.append(
                        {'start': seed_range['start'], 'end': o['start']})
                    if o['end'] >= seed_range['end']:
                        new_ranges.append(
                            {'start': o['start'] + o['convert'], 'end': seed_range['end'] + o['convert']})
                        seed_range = None
                    elif o['end'] < seed_range['end']:
                        new_ranges.append(
                            {'start': o['start'] + o['convert'], 'end': o['end'] + o['convert']})
                        seed_range = {
                            'start': o['end'] + 1, 'end': seed_range['end']}
            if seed_range:
                new_ranges.append(seed_range)
        else:
            new_ranges.append(seed_range)


sorted_ranges = sorted(new_ranges, key=lambda x: (x['start']))
print('Answer to part 2:', sorted_ranges[0]['start'])

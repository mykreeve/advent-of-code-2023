file = open('./input/day15input.txt')
file = file.read().split(',')


def calc_score(item):
    score = 0
    for ch in item:
        score += ord(ch)
        score *= 17
        score %= 256
    return score


sum = 0
for item in file:
    score = calc_score(item)
    sum += score

print('Answer to part 1:', sum)

boxes = {}


def update_item(items, name, label):
    updated = []
    for item in items:
        if item['name'] == name:
            updated.append({'name': name, 'label': label})
        else:
            updated.append(item)
    return updated


for item in file:
    if '=' in item:
        item = item.split('=')
        label = int(item[1])
        name = item[0]
        score = calc_score(name)
        if score not in boxes:
            boxes[score] = [{'name': name, 'label': label}]
        else:
            test = list(filter(lambda x: x['name'] == name, boxes[score]))
            if len(test) > 0:
                boxes[score] = update_item(boxes[score], name, label)
            else:
                boxes[score].append({'name': name, 'label': label})
    elif '-' in item:
        name = item.replace('-', '')
        score = calc_score(name)
        if score in boxes:
            boxes[score] = list(
                filter(lambda x: x['name'] != name, boxes[score]))

score = 0
for box in boxes:
    box_val = box + 1
    box_contents = boxes[box]
    for index, b in enumerate(box_contents):
        box_position = index + 1
        box_label = b['label']
        score += (box_val * box_position * box_label)
        # print(box_val, box_position, box_label,
        #       b['name'], '=', box_val * box_position * box_label, '  -> ', score)

print('Answer to part 2:', score)

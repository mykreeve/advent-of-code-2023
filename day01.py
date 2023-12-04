file = open('./input/day1input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

tot = 0
for f in file:
    current = ''
    for pos in range(len(f)):
        if f[pos] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            current += f[pos]
            break
    for pos in range(len(f)-1, -1, -1):
        if f[pos] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            current += f[pos]
            break
    tot += int(current)

print('Answer to part 1:', tot)

lookups = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

tot = 0
for f in file:
    numbers = ''
    pos = 0
    while pos < len(f):
        if f[pos] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            numbers += f[pos]
            pos += 1
        else:
            for l in lookups:
                if (pos + len(l)) > len(f):
                    continue
                test = f[pos:pos+len(l)]
                if test == l:
                    numbers += lookups[l]
                    pos += 1
                    continue
            pos += 1
    # print(f, int(numbers[0] + numbers[len(numbers)-1]))
    # input('.')
    tot += int(numbers[0] + numbers[len(numbers)-1])

print('Answer to part 2:', tot)

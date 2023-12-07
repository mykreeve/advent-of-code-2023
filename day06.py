from functools import reduce

file = open('./input/day6input.txt')
file = file.readlines()
file = list(map(lambda x: x.replace('\n', ''), file))

times = file[0].replace('Time:       ', '').strip().split(' ')
times = list(filter(lambda x: x != '', times))
times = list(map(lambda x: int(x), times))

distances = file[1].replace('Distance: ', '').strip().split(' ')
distances = list(filter(lambda x: x != '', distances))
distances = list(map(lambda x: int(x), distances))

ways = []

for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    succ = 0
    for charge_time in range(time):
        speed = charge_time
        achieve_distance = speed * (time - charge_time)
        if achieve_distance > distance:
            succ += 1
    ways.append(succ)

print('Answer to part 1:', reduce((lambda x, y: x * y), ways))


time = int(file[0].replace('Time:', '').replace(' ', ''))

distance = int(file[1].replace('Distance:', '').replace(' ', ''))

succ = 0
for charge_time in range(time):
    speed = charge_time
    achieve_distance = speed * (time - charge_time)
    if achieve_distance > distance:
        succ += 1

print('Answer to part 2:', succ)

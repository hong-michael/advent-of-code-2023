with open("input.txt") as f:
    lines = f.read()

input = lines.splitlines()
result = 1  # We can assume the existence of a solution.

## Part 1
time = input[0].split()[1:]
distance = input[1].split()[1:]

def can_beat(speed, i):
    return (int(time[i]) - speed) * speed > int(distance[i])

for i in range(len(time)):
    ways = 0
    for j in range(int(time[i])):
        if can_beat(j, i):
            ways += 1
    result *= ways

print(result)

## Part 2
time_2 = ''.join(input[0].split()[1:])
distance_2 = ''.join(input[1].split()[1:])
ways_2 = 0

for i in range(int(time_2)):
    if (int(time_2) - i) * i > int(distance_2):
        ways_2 += 1

print(ways_2)





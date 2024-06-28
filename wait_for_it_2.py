with open("input.txt") as f:
    lines = f.read()

# TODO: Are the 3 letters on the LHS of each input line unique? If so then use hash map.
input = lines.splitlines()  # Coordinates start at input[2].
result = 0  

directions = input[0]
hash_map = {}

## Part 1
for i in range(2, len(input)):
    tuple = input[i].split('(')[1].split(')')[0]
    hash_map[input[i].split(' = ')[0]] = (tuple.split(', ')[0], tuple.split(', ')[1])

curr = "AAA"  # Initialization of curr.

while curr != "ZZZ":
    for d in directions:
        if curr == "ZZZ":
            break
        if d == "L":
            curr = hash_map[curr][0]  # Need to fix the format of the dict value so that it's an indexable tuple.
        elif d == "R":
            curr = hash_map[curr][1]
        result += 1

print(result)

## Part 2







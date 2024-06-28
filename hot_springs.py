with open("input.txt") as f:
    lines = f.read()

# TODO: Are the 3 letters on the LHS of each input line unique? If so then use hash map.
input = lines.splitlines()  # Coordinates start at input[2].
result = 0  

for i in input:
    onsen, groups = i.split()  # Every line has at least some damaged onsen.
    possible_count = onsen.count('?') + onsen.count('#')
    possible = ['?', '#']
    









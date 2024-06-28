with open("input.txt") as f:
    lines = f.read()

input = lines.splitlines()
result = 0

for i in input:
    max_colors = {"red": 0, "green": 0, "blue": 0}
    ID, rest = i.split(":")
    games = rest.split(";")
    for g in games:
        draws = g.split(",")
        for d in draws:
            num_colors = d.split()
            max_colors[num_colors[1]] = max(int(num_colors[0]), max_colors[num_colors[1]])
    result += max_colors["red"] * max_colors["green"] * max_colors["blue"]

print(result)

                





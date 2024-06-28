with open("input.txt") as f:
    lines = f.read()

input = lines.splitlines()
result = 0

max_colors = {"red": 12, "green": 13, "blue": 14}
for i in input:
    ID, rest = i.split(":")
    games = rest.split(";")
    flag = True
    for g in games:
        draws = g.split(",")
        for d in draws:
            num_colors = d.split()
            # 12 red, 13 green, 14 blue
            if int(num_colors[0]) > max_colors[num_colors[1]]:
                flag = False
                break
        if not flag:
            break
    if flag:
        result += int(ID.split()[1])

print(result)

                





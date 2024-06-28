with open("input.txt") as f:
    lines = f.read()

input = lines.splitlines()
result = 0

## Part 1
for i in input:
    # Naive solution? O(|card| * |scratchcard| * num_cards)
    card, scratchcard = i.split(':')[1].split('|')
    points_i = -1
    for c in card.split():
        if c in scratchcard.split():
            points_i += 1    
    if points_i >= 0:
        result += 2 ** points_i

print(result)

## Part 2
multipliers = [1 for i in range(len(input))]

for idx, i in enumerate(input):
    card, scratchcard = i.split(':')[1].split('|')
    points_i = 0
    for c in card.split():
        if c in scratchcard.split():
            points_i += 1 
    for j in range(points_i):
        multipliers[idx + j + 1] += multipliers[idx] * 1

total_cards = sum(multipliers)
print(total_cards)
# print(multipliers)






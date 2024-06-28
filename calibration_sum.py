with open("input.txt") as f:
    input = f.read().splitlines()

total_sum = 0
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for i in range(len(input)):
    curr_num = ""
    curr_indexes = []

    for idx, char in enumerate(input[i]):
        if char.isnumeric():
            curr_num += char
            curr_indexes.append(idx)

    if curr_num:
        temp_num = [curr_num[0], curr_num[-1]]
    else: 
        temp_num = ["0", "0"]

    if not curr_indexes:
        curr_indexes.append(len(input[i]) - 1)
        curr_indexes.append(0)

    min_index, max_index = float("inf"), -1
    first_num, last_num = "", ""

    for num in numbers:
        if num in input[i][0:curr_indexes[0]]:
            if input[i].index(num) < min_index:
                min_index = input[i].index(num)
                first_num = num

    for num in numbers:
        if num in input[i][curr_indexes[-1]:]:
            if input[i].rindex(num) > max_index:
                max_index = input[i].rindex(num)
                last_num = num

    if min_index < float("inf"):
        temp_num[0] = str(numbers[first_num])
    if max_index >= 0:
        temp_num[1] = str(numbers[last_num])  

    total_sum += int(''.join(temp_num))

print(total_sum)




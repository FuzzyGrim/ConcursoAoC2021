# Part 1
with open("input.txt") as file:
    data = file.read().split('\n')

horizontal = 0
depth = 0

for i in range(0, len(data) - 1):
    
    data[i] = data[i].split()

    if data[i][0] == "forward":
        horizontal += int(data[i][1])

    elif data[i][0] == "up":
        depth -= int(data[i][1])

    else:
        depth += int(data[i][1])

print(depth * horizontal)


# Part 2
horizontal = 0
depth = 0
aim = 0

for i in range(0, len(data) - 1):
    
    if data[i][0] == "forward":
        horizontal += int(data[i][1])
        depth += int(data[i][1]) * aim 

    elif data[i][0] == "up":
        aim -= int(data[i][1])

    else:
        aim += int(data[i][1])

print(depth * horizontal)

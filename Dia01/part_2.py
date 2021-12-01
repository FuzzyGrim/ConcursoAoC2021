with open("input.txt") as file:
    data = file.read().split('\n')

increased = 0

for i in range(0, len(data) - 4):
    sum_1 = int(data[i])
    sum_2 = int(data[i+3])
    if sum_2 > sum_1:
        increased += 1

data = open('input.txt', 'r').read().split('\n')

increased = 0

for i in range(0, len(data) - 4):
    sum_1 = int(data[i]) + int(data[i+1]) + int(data[i+2])
    sum_2 = int(data[i+1]) + int(data[i+2]) + int(data[i+3])
    if sum_2 > sum_1:
        increased += 1

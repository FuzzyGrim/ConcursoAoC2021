with open("input.txt") as file:
    data = file.read().splitlines()

increased = 0

for i in range(0, len(data) - 1):
    if int(data[i+1]) > int(data[i]):
        increased += 1

print(increased)



increased = 0

for i in range(0, len(data) - 3):
    sum_1 = int(data[i])
    sum_2 = int(data[i+3])
    if sum_2 > sum_1:
        increased += 1

print(increased)

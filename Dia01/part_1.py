with open("input.txt") as file:
    data = file.read().split('\n')

increased = 0

for i in range(0, len(data) - 2):
    if int(data[i+1]) > int(data[i]):
        increased += 1

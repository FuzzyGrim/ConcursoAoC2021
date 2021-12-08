import copy

# Naive :)
def part1(data):

    date = 1

    while date <= 18:

        for day in range(0, len(data)):
            if data[day] > 0:
                data[day] -= 1
            elif data[day] == 0:
                data[day] = 6
                data.append(8)

        date += 1

    return len(data)


def part2(data):
    fish = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for num in data:
        fish[num] += 1

    date = 1

    while date <= 256: 
        add_6_8 = 0
        for key in fish:
            if key == 0:
                if fish[key] > 0:
                    add_6_8 = fish[key]
                    fish[key] = 0
            elif key > 0:
                if fish[key] > 0:
                    fish[key - 1] += fish[key]
                    fish[key] = 0
        fish[6] += add_6_8
        fish[8] += add_6_8
        date += 1

    return sum(fish.values())



with open("input.txt") as file:
    data = file.read().splitlines()

data = data[0].split(',')
data = list(map(int, data))
data2 = copy.deepcopy(data)

print(part1(data))
print(part2(data2))

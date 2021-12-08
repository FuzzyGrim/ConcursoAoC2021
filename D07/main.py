def part1(maximum, minimum):
    cost_to_min = 0
    for num in data:
        cost_to_min += abs(num - minimum)

    result = cost_to_min

    while minimum < maximum:
        cost = 0
        for num in data:
            cost += abs(num - minimum)
        if cost < result:
            result = cost
        minimum += 1

    print(result)

def part2(maximum, minimum):
    cost_to_min = 0
    for num in data:
        diff = abs(num - minimum)
        cost_to_min += (diff * (diff + 1))/2

    result = cost_to_min

    while minimum < maximum:
        cost = 0
        for num in data:
            diff = abs(num - minimum)
            cost += (diff * (diff + 1))/2
        if cost < result:
            result = cost
        minimum += 1

    print(result)



with open("input.txt") as file:
    data = file.read().splitlines()

data = data[0].split(',')
data = list(map(int, data))

minimum = min(data)
maximum = max(data)

part1(maximum, minimum)
part2(maximum, minimum)

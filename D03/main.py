with open("input.txt") as file:
    data = file.read().splitlines()

# PART 1
gamma = ""
epsilon = ""

num_digits = len(data[0])
for digit in range(0, num_digits):
    nums_of_1 = 0
    nums_of_0 = 0
    num = 0
    while num < len(data):
        if data[num][digit] == "1":
            nums_of_1 += 1
        else:
            nums_of_0 += 1
        num += 1
    if nums_of_1 > nums_of_0:
        gamma = gamma + str(1)
        epsilon = epsilon + str(0)
    else:
        gamma = gamma + str(0)
        epsilon = epsilon + str(1)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)



# PART 2
max_bits = data
min_bits = data
for digit in range(0, num_digits):
    list_0 = []
    list_1 = []
    num = 0
    while num < len(max_bits):
        if max_bits[num][digit] == "1":
            list_1.append(max_bits[num])
        else:
            list_0.append(max_bits[num])
        num += 1

    if len(list_1) > len(list_0):
        max_bits = list_1
    elif len(list_0) > len(list_1):
        max_bits = list_0
    elif len(list_1) == len(list_0):
        max_bits = list_1

    if len(max_bits) == 1:
        oxygen = max_bits

    list_0 = []
    list_1 = []
    num = 0
    while num < len(min_bits):
        if min_bits[num][digit] == "1":
            list_1.append(min_bits[num])
        else:
            list_0.append(min_bits[num])
        num += 1

    if len(list_1) < len(list_0):
        min_bits = list_1
    elif len(list_0) < len(list_1):
        min_bits = list_0
    elif len(list_1) == len(list_0):
        min_bits = list_0

    if len(min_bits) == 1:
        co2 = min_bits

oxygen = int(oxygen[0],2)
co2 = int(co2[0],2)

print(oxygen * co2)

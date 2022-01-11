def hevalueadecimal_to_binary(letter):
    transform = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    return transform[letter]


def parse(data):
    # global VERSION_TOTAL
    # version = int(data[:3], 2)
    # VERSION_TOTAL += version

    id = int(data[3:6], 2)

    data = data[6:]

    if id == 4:
        t = ""
        while True:
            t += data[1:5]
            prefivalue = data[0]
            data = data[5:]
            if prefivalue == "0":
                break
        return (data, int(t, 2))

    else:
        length_type_ID = data[0]
        data = data[1:]
        sub_packet_values = []
        if length_type_ID == "0":
            subpackets_length_bits = int(data[0:15], 2)
            data = data[15:]
            subpackets = data[:subpackets_length_bits]
            while subpackets:
                subpackets, value = parse(subpackets)
                sub_packet_values.append(value)
            data = data[subpackets_length_bits:]

        else:
            sub_packets_num = int(data[:11], 2)
            data = data[11:]
            for i in range(sub_packets_num):
                data, value = parse(data)
                sub_packet_values.append(value)

        if id == 0:
            return (data, sum(sub_packet_values))
        if id == 1:
            p = 1
            for value in sub_packet_values:
                p *= value
            return (data, p)
        if id == 2:
            return (data, min(sub_packet_values))
        if id == 3:
            return (data, max(sub_packet_values))
        if id == 5:
            return (data, 1 if sub_packet_values[0] > sub_packet_values[1] else 0)
        if id == 6:
            return (data, 1 if sub_packet_values[0] < sub_packet_values[1] else 0)
        if id == 7:
            return (data, 1 if sub_packet_values[0] == sub_packet_values[1] else 0)


with open("input.txt") as file:
    data = file.read().splitlines()

binary_string = ""
for letter in data[0]:
    binary_string += hevalueadecimal_to_binary(letter)

VERSION_TOTAL = 0

# print(VERSION_TOTAL)
print(parse(binary_string)[1])

def part1(data):
    result = 0
    for count, letters in enumerate(data):
        data[count] = letters.split(" | ")
        data[count][1] = data[count][1].split(" ")
        for output in data[count][1]:
            if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
                result += 1
    return result


def part2(data):
    output_total = 0
    for entry in range(0, len(data)):
        data[entry][0] = data[entry][0].split(" ")
        mappings = {}
        for output in data[entry][0]:
            if len(output) == 2:
                mappings["1"] = output
            elif len(output) == 3:
                mappings["7"] = output
            elif len(output) == 4:
                mappings["4"] = output
            elif len(output) == 7:
                mappings["8"] = output

        for output in data[entry][0]:
            if len(output) == 5:
                if mappings["1"][0] in output and mappings["1"][1] in output:
                    mappings["3"] = output

            elif len(output) == 6:
                if mappings["1"][0] not in output or mappings["1"][1] not in output:
                    mappings["6"] = output
                elif mappings["4"][0] in output and mappings["4"][1] in output and mappings["4"][2] in output and mappings["4"][3] in output:
                    mappings["9"] = output
                else:
                    mappings["0"] = output


        for output in data[entry][0]:
            if len(output) == 5:
                if output[0] in mappings["6"] and output[1] in mappings["6"] and output[2] in mappings["6"] and output[3] in mappings["6"] and output[4] in mappings["6"]:
                    mappings["5"] = output
                elif output != mappings["3"]:
                    mappings["2"] = output

        result = ""
        for output in data[entry][1]:
            if len(output) == 2:
                result += "1"
            elif len(output) == 3:
                result += "7"
            elif len(output) == 4:
                result += "4"
            elif len(output) == 7:
                result += "8"
            elif len(output) == 5:
                match_list = all([characters in mappings["2"] for characters in output])
                if match_list:
                    result += "2"
                match_list = all([characters in mappings["3"] for characters in output])
                if match_list:
                    result += "3"
                match_list = all([characters in mappings["5"] for characters in output])
                if match_list:
                    result += "5"
            elif len(output) == 6:
                match_list = all([characters in mappings["0"] for characters in output])
                if match_list:
                    result += "0"
                match_list = all([characters in mappings["6"] for characters in output])
                if match_list:
                    result += "6"
                match_list = all([characters in mappings["9"] for characters in output])
                if match_list:
                    result += "9"
        output_total += int(result)

    return output_total


with open("input.txt") as file:
    data = file.read().splitlines()

print(part1(data))
print(part2(data))



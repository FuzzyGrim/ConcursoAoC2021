def get_low_points(data):
    basins = []
    low_points = []

    for count, sublist in enumerate(data):
        if count == 0:
            for index, num in enumerate(sublist):
                if index == 0:
                    if num < sublist[index + 1] and num < data[count + 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))
                        
                elif index == len(sublist) - 1:
                    if num < sublist[index - 1] and num < data[count + 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))

                else:
                    if num < sublist[index - 1] and  num < sublist[index + 1] and num < data[count + 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))

        
        elif count == len(data) - 1:
            for index, num in enumerate(sublist):
                if index == 0:
                    if num < sublist[index + 1] and num < data[count - 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))


                elif index == len(sublist) - 1:
                    if num < sublist[index - 1] and num < data[count - 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))

                else:
                    if num < sublist[index - 1] and  num < sublist[index + 1] and num < data[count - 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))

        else:
            for index, num in enumerate(sublist):
                if index == 0:
                    if num < sublist[index + 1] and num < data[count - 1][index]  and num < data[count + 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))


                elif index == len(sublist) - 1:
                    if num < sublist[index - 1] and num < data[count - 1][index] and num < data[count + 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))


                else:
                    if num < sublist[index - 1] and num < sublist[index + 1] and num < data[count - 1][index] and num < data[count + 1][index]:
                        low_points.append(num)
                        basins.append(get_basin(data, count, index))

    sum = 0
    for i in low_points:
        sum += i + 1
    print("Total low points: " + str(sum))


    basins = sorted(basins, reverse=True)
    print("Basins result: " + str(basins[0] * basins[1] * basins[2]))
    return low_points

def get_basin(data, i, j):
    if 0 <= i < len(data) and 0 <= j < len(data[i]) and data[i][j] != 9:
        data[i][j] = 9
        return (1 + get_basin(data, i - 1, j) + get_basin(data, i + 1, j) + get_basin(data, i, j - 1) + get_basin(data, i, j + 1))
    return 0


with open("input.txt") as file:
    data = file.read().splitlines()

for count, number in enumerate(data):
    data[count] = [int(x) for x in number]

get_low_points(data)

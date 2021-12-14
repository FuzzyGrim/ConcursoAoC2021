with open("input.txt") as file:
    data = file.read().splitlines()

coordinates_list = []
folds = []

width = 0
height = 0

for n, item in enumerate(data):
    if item == "":
        folds = data[n+1:]
        break
    else:
        item = item.split(",")
        item[0] = int(item[0])
        item[1] = int(item[1])
        if item[0] > width: width = item[0]
        if item[1] > height: height = item[1]
        coordinates_list.append(item)

matrix = [['.' for x in range(width + 1)] for y in range(height + 1)]

for coordinates in coordinates_list:
    x = coordinates[0]
    y = coordinates[1]
    matrix[y][x] = "#"

for i, fold in enumerate(folds):
    fold_num = int((fold.split("="))[1])
    if "x" in fold: 
        fold_axis = "x"
    else:
        fold_axis = "y"

    if fold_axis == "y":
        matrix_keep_part = matrix[:fold_num]
        matrix_throw_part = matrix[fold_num + 1:]
        for y in range(len(matrix_throw_part)):
            for x in range(len(matrix_throw_part[0])):
                if matrix_throw_part[y][x] == "#":
                    if matrix_keep_part[len(matrix_keep_part) - (y + 1)][x] != "#":
                        matrix_keep_part[len(matrix_keep_part) - (y + 1)][x] = "#"
    elif fold_axis == "x":
        matrix_keep_part = []
        matrix_throw_part = []
        for array in matrix:
            matrix_keep_part.append(array[:fold_num])
            matrix_throw_part.append(array[fold_num+1:])
        for y in range(len(matrix_throw_part)):
            for x in range(len(matrix_throw_part[0])):
                if matrix_throw_part[y][x] == "#":
                    if matrix_keep_part[y][len(matrix_keep_part[0]) - (x + 1)] != "#":
                        matrix_keep_part[y][len(matrix_keep_part[0]) - (x + 1)] = "#"

    if i == 0:
        dots_count = 0
        for y in range(len(matrix_keep_part)):
            for x in range(len(matrix_keep_part[0])):
                if matrix_keep_part[y][x] == "#":
                    dots_count += 1
        print(dots_count)
    
    matrix = matrix_keep_part

for y in range(len(matrix)):
        print(matrix[y])
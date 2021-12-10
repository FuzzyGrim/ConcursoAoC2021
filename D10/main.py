with open("input.txt") as file:
    data = file.read().splitlines()

brackets = 0
square_br = 0
curly_br = 0
less = 0

lines_to_elim = []
for line_num, line in enumerate(data):

    elim_count = 0
    data[line_num] = list(line)

    for index, sign in enumerate(line):
        if sign == ")" or sign =="]" or sign == "}" or sign == ">":
            
            if sign == ")" and data[line_num][index + (- 1 - elim_count)] != "(":
                brackets += 1
                lines_to_elim.append(line_num)
                break
            elif sign == "]" and data[line_num][index + (- 1 - elim_count)] != "[":
                square_br += 1
                lines_to_elim.append(line_num)
                break
            elif sign == "}" and data[line_num][index + (- 1 - elim_count)] != "{":
                curly_br += 1
                lines_to_elim.append(line_num)
                break
            elif sign == ">" and data[line_num][index + (- 1 - elim_count)] != "<":
                less += 1
                lines_to_elim.append(line_num)
                break
            else:
                del data[line_num][index - elim_count]
                del data[line_num][index + (- 1 - elim_count)]
                elim_count += 2


print(brackets * 3 + square_br * 57 + curly_br * 1197 + less * 25137)

# Discard corrupted lines
for line in reversed(lines_to_elim):
    del data[line]

points_per_line = []
for line_num, line in enumerate(data):
    points = 0
    for sign in reversed(line):
        if sign == "(":
            data[line_num].append(")")
            points = points * 5 + 1
        elif sign == "[":
            data[line_num].append("]")
            points = points * 5 + 2
        elif sign == "{":
            data[line_num].append("}")
            points = points * 5 + 3
        elif sign == "<":
            data[line_num].append(">")
            points = points * 5 + 4
    points_per_line.append(points)

points_per_line = sorted(points_per_line)
print(points_per_line[int(len(points_per_line) / 2)])
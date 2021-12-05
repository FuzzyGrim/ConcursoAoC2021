import re

def isBingo(board):
    for row in board:
        bingo_row = True
        for num in row:
            if num != "x":
                bingo_row = False
        if bingo_row:
            return True
    row_len = len(board[0])
    for digit in range(0, row_len):
        bingo_column = True
        for row in board:
            if row[digit] != "x":
                bingo_column = False
        if bingo_column:
            return True

    return False

def refactor_data(data):
    grouped_list = []

    for line in data:
        if line != "":
            grouped_list.append([])

    index = 0

    for line in data:
        if line == "":
            index += 1
        else:
            grouped_list[index].append(line)

    index_empty = 0
    while grouped_list[index_empty] != []:
        index_empty += 1
    del grouped_list[index_empty:]

    for board in grouped_list:
        for row in range(0, len(board)):
            # \s+: replace consecutive whitespace characters using the regular expression
            board[row] = re.sub("\s+", ",", board[row].strip())
            board[row] = list(board[row].split(","))
    return grouped_list




def part1():

    for drawed_num in nums_to_draw:
        for board_count, board in enumerate(grouped_list):
            for row in board:
                for num in range(0, len(row)):
                    if row[num] == drawed_num:
                        row[num] = 'x'
                
            for board in range(0, len(grouped_list)):
                result = isBingo(grouped_list[board])
                
                if result == True:
                    sum = 0
                    for row in grouped_list[board_count]:
                        for num in row:
                            if num != 'x':
                                sum += int(num)
                    return (sum * int(drawed_num))

def part2():

    boards_completed = set()

    for drawed_num in nums_to_draw:
        for board_count, board in enumerate(grouped_list):
            for row in board:
                for num in range(0, len(row)):
                    if row[num] == drawed_num:
                        row[num] = 'x'
                
        for board in range(0, len(grouped_list)):

            if board not in boards_completed:

                result = isBingo(grouped_list[board])
                
                if result == True:
                    if len(grouped_list) - 1 > len(boards_completed):
                        boards_completed.add(board)

                    elif len(grouped_list) - 1 == len(boards_completed):
                        sum = 0
                        for row in grouped_list[board]:
                            for num in row:
                                if num != 'x':
                                    sum += int(num)
                        return (sum * int(drawed_num))

with open("input.txt") as file:
    data = file.read().splitlines()

grouped_list = refactor_data(data)

nums_to_draw = grouped_list[0][0]
del grouped_list[0]

print(part1())
print(part2())

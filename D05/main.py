def coords_vert_hor(coords, coords_dict):
    coords = list(map(lambda x: x.split(","), coords))
    start_x = int(coords[0][0])
    end_x = int(coords[1][0])
    start_y = int(coords[0][1])
    end_y = int(coords[1][1])

    # vertical line
    if start_y == end_y:
        if start_x < end_x:
            while start_x <= end_x:
                add_to_coords_dict(start_x, end_y, coords_dict)
                start_x += 1
        else:
            while end_x <= start_x:
                add_to_coords_dict(start_x, end_y, coords_dict)
                start_x -= 1
    
    # horizontal line
    elif start_x == end_x:
        if start_y < end_y:
            while start_y <= end_y:
                add_to_coords_dict(start_x, start_y, coords_dict)
                start_y += 1
        elif end_y < start_y:
            while end_y <= start_y:
                add_to_coords_dict(start_x, start_y, coords_dict)
                start_y -= 1

def coords_vert_hor_diag(coords, coords_dict):
    coords = list(map(lambda x: x.split(","), coords))
    start_x = int(coords[0][0])
    end_x = int(coords[1][0])
    start_y = int(coords[0][1])
    end_y = int(coords[1][1])

    # vertical line
    if start_y == end_y:
        if start_x < end_x:
            while start_x <= end_x:
                add_to_coords_dict(start_x, end_y, coords_dict)
                start_x += 1
        else:
            while end_x <= start_x:
                add_to_coords_dict(start_x, end_y, coords_dict)
                start_x -= 1
    
    # horizontal line
    elif start_x == end_x:
        if start_y < end_y:
            while start_y <= end_y:
                add_to_coords_dict(start_x, start_y, coords_dict)
                start_y += 1
        elif end_y < start_y:
            while end_y <= start_y:
                add_to_coords_dict(start_x, start_y, coords_dict)
                start_y -= 1
    
    # diagonal "/"
    elif (start_x - end_x) == (start_y - end_y):
        if (start_x > end_x) and (start_y > end_y):
            while (start_x >= end_x) and (start_y >= end_y):
                add_to_coords_dict(start_x, start_y, coords_dict)
                start_x -= 1
                start_y -= 1
        elif (start_x < end_x) and (start_y < end_y):
            while (start_x <= end_x) and (start_y <= end_y):
                add_to_coords_dict(start_x, start_y, coords_dict)
                start_x += 1
                start_y += 1

    # diagonal "\"
    elif -(start_x - end_x) == (start_y - end_y):
        if (start_x > end_x) and (start_y < end_y):
            while (start_x >= end_x) and (start_y <= end_y):
                add_to_coords_dict(start_x, start_y, coords_dict)
                start_x -= 1
                start_y += 1
        elif (start_x < end_x) and (start_y > end_y):
            while (start_x <= end_x) and (start_y >= end_y):
                add_to_coords_dict(start_x, start_y, coords_dict)
                start_x += 1
                start_y -= 1

def add_to_coords_dict(x, y, coords_dict):
    coords = [str(x), str(y)]
    coords_to_add = ",".join(coords)
    if not coords_to_add in coords_dict:
        coords_dict[coords_to_add] = 1
    else:
        coords_dict[coords_to_add] += 1
    

def part_1():
    coords_dict = {}
    for sublist in data:
        coords_vert_hor(sublist, coords_dict)

    points = 0

    for number in coords_dict.values():
        if number > 1:
            points += 1

    return points


def part_2():
    coords_dict = {}
    for sublist in data:
        coords_vert_hor_diag(sublist, coords_dict)

    points = 0

    for number in coords_dict.values():
        if number > 1:
            points += 1

    return points


with open("input.txt") as file:
    data = file.read().splitlines()

data = list(map(lambda x: x.split(" -> "), data))

print(part_1())
print(part_2())

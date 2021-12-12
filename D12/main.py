import copy

def count_paths(start, visited, part):
    if start == "end":
        return 1
    
    count = 0

    for destination in paths[start]:
        if destination.islower():
            if destination not in visited:
                count += count_paths(destination, visited | {destination}, part)

            elif part == 2 and destination not in {'start', 'end'}:
                count += count_paths(destination, visited | {destination}, part=1)
        else:
            count += count_paths(destination, visited, part)

    return count


with open("input.txt") as file:
    data = file.read().splitlines()
data_copy = copy.deepcopy(data)

for i, connection in enumerate(data):
    data_copy[i] = connection.split("-")
    data_copy.append(data_copy[i][::-1])

data = copy.deepcopy(data_copy)
paths = {}

# Create paths, eg: {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'b': ['d', 'end']}
for connection in data:
    if connection[0] in paths:
        paths[connection[0]].append(connection[1])

    else:
        paths[connection[0]] = [connection[1]]

print(count_paths("start", {"start"}, part=1))
print(count_paths("start", {"start"}, part=2))
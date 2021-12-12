with open("input.txt") as file:
    data = file.read().splitlines()

for count, number in enumerate(data):
    data[count] = [int(x) for x in number]

steps = 0
count = 0

while True:

    steps += 1

    for i, sublist in enumerate(data):
        for j, num in enumerate(data[i]):
            data[i][j] += 1


    while True:
        updated = False
        for i, sublist in enumerate(data):
            for j, num in enumerate(data[i]):
                if data[i][j] > 9:
                    data[i][j] = - 999
                    updated = True
                    count += 1
                    for di,dj in [[-1,1], [0,1], [1,1], [-1,0], [1,0], [-1,-1], [0,-1], [1,-1]]:
                        ni,nj = i+di, j+dj
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            if data[ni][nj] != 10 and data[ni][nj] != 0:
                                data[ni][nj] += 1
        
        if not updated:
            break
    
    all_flash = True
    for i, sublist in enumerate(data):
        for j, num in enumerate(data[i]):
            if data[i][j] < 0:
                data[i][j] = 0
            else:
                all_flash = False
    
    if all_flash: 
        break

print(count)
print(steps)

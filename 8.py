import copy

f = open("./info/8.txt", "r")

lines = f.read().splitlines()

for y in range(len(lines)):
    lines[y] = list(lines[y])

dupl = copy.deepcopy(lines)
east = copy.deepcopy(lines)
west = copy.deepcopy(lines)
north = copy.deepcopy(lines)
south = copy.deepcopy(lines)



for y in range(len(west)):
    largestN = largestE = largestS = largestW = -1
    for x in range(len(west[y])):
        if int(west[y][x]) > largestW:
            largestW = int(west[y][x])
        else:
            west[y][x] = -1
        if int(north[x][y]) > largestN:
           largestN = int(north[x][y])
        else:
            north[x][y] = -1
        if int(east[y][-x-1]) > largestE:
            largestE = int(east[y][-x-1])
        else:
            east[y][-x-1] = -1
        if int(south[-x-1][y]) > largestS:
          largestS = int(south[-x-1][y])
        else:
           south[-x-1][y] = -1

for y in range(len(west)):
    for x in range(len(west[y])):
        if type(north[y][x]) == str:
            lines[y][x] = north[y][x]
        elif type(east[y][x]) == str:
            lines[y][x] = east[y][x]
        elif type(south[y][x]) == str:
            lines[y][x] = south[y][x]
        elif type(west[y][x]) == str:
            lines[y][x] = west[y][x]
        else:
            lines[y][x] = -1
        
count = 0
for y in range(len(lines)):
    for x in range(len(lines)):
        if type(lines[y][x]) == str:
            count += 1
print(count)

countN = countE = countW = countS = 0

for y in range(len(dupl)):
    for x in range(len(dupl[x]))
        

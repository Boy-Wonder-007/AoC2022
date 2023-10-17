f = open("./info/7.txt", "r")

lines = f.read().splitlines()
splitLines = []

for x in lines:
    splitLines.append(x.split())

count = 0

for x in range(len(splitLines)):
    if splitLines[x][0] == "$":
        splitLines[x].pop(0)

    if splitLines[x][0] == "ls":
        count += 1

for x in range(len(splitLines)-count):
    if splitLines[x][0] == "ls":
        splitLines.pop(x)
    
compPathway = []
folderChain = []
folderSizes = [[],[],[]]

for x in range(len(splitLines)):
    if splitLines[x][0] == "cd" and splitLines[x][1] != "..":
        folderChain.append(splitLines[x][1])
        compPathway.append(folderChain[len(folderChain)-1])
        folderSizes[0].append(splitLines[x][1])
        folderSizes[1].append(0)
        folderSizes[2].append(len(folderChain))
    elif splitLines[x][0] == "cd" and splitLines[x][1] == "..":
        folderChain.pop(len(folderChain)-1)
        compPathway.append(folderChain[len(folderChain)-1])
    elif splitLines[x][0].isnumeric() == True:
        folderSizes[1][len(folderSizes[1])-1] += int(splitLines[x][0])

folderCurrent = ""
dirSize = 0

folderSizes[0].reverse()
folderSizes[1].reverse()
folderSizes[2].reverse()

for x in range(len(folderSizes[0])):
    folderCurrent = folderSizes[2][x]
    dirSize = folderSizes[1][x]
    for y in range(len(folderSizes[2][x:])):
        if folderCurrent > folderSizes[2][x+y]:
            folderSizes[1][x+y] += dirSize
            break

total = 0

for x in folderSizes[1]:
    if x < 100000:
        total += x

print(total)

spaceNeeded = -(70000000-30000000-folderSizes[1][-1])
print(spaceNeeded)
files = []
fileList = []

for x in range(len(folderSizes[1])):
    if folderSizes[1][x] > spaceNeeded:
        fileList.append(folderSizes[1][x])
        files.append(folderSizes[0][x])
    
print(files, fileList)
fileList.sort()
print(fileList)
##while x < len(folderSizes[0]):
##    if folderSizes[2][x] > len(nameChain):
##        nameChain.append(folderSizes[0][x])
##    else:
##        while y < len(folderSizes[0]):
##            if len(nameChain) == folderSizes[2][y] and nameChain[-1] == folderSizes[0][y]:
##                dirSize = folderSizes[1][y]
##            y += 1
##        y = 0
##        nameChain.pop(len(nameChain)-1)
##        while y < len(folderSizes[0]):
##            if len(nameChain) == folderSizes[2][y] and nameChain[-1] == folderSizes[0][y]:
##                folderSizes[1][y] += dirSize
##            y += 1
##        y=0
##        dirSize = 0
##        
##        x -= 1
##        
##    dirSize = 0
##    
##    x += 1
##
##
##for x in folderSizes[1]:
##    if x <= 100000:
##        print(dirSize)
##        dirSize += x
##
##print(dirSize)

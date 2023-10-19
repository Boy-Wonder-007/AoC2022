def readFile():
    f = open("./info/3.txt", "r")

    lines = f.read().splitlines()
    return lines

def checkElf(lines):
    finalArray = []

    for x in lines:
        s1 = set(x[:len(x)//2])
        s2 = set(x[len(x)//2:])
        finalArray.append(str(s1 & s2))
    return finalArray

def calcTotal1(finalArray):
    total = 0

    for x in finalArray:
        if ord(x[2]) < 91:
            total += ord(x[2])-38
        else:
            total += ord(x[2])-96
    return total

def compElves(lines):
    
    finalArray = []

    for y in range(int(len(lines)/3)):
        y *= 3
        s1 = set(lines[y])
        s2 = set(lines[y+1])
        s3 = set(lines[y+2])
        finalArray.append(str(s1 & s2 & s3 ))
    return finalArray

lines = readFile()
finalArray = checkElf(lines)
total1 = calcTotal1(finalArray)
finalArray = compElves(lines)
total2 = calcTotal1(finalArray)
print(total1, total2)

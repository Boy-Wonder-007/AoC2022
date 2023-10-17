f = open("./info/3.txt", "r")

lines = f.read().splitlines()
finalArray = []

for x in lines:
    s1 = set(x[:len(x)//2])
    s2 = set(x[len(x)//2:])
    finalArray.append(str(s1 & s2))

total = 0

for x in finalArray:
    if ord(x[2]) < 91:
        total += ord(x[2])-38
    else:
        total += ord(x[2])-96

print(total)

finalArray = []
total = 0

for y in range(int(len(lines)/3)):
    y *= 3
    s1 = set(lines[y])
    s2 = set(lines[y+1])
    s3 = set(lines[y+2])
    finalArray.append(str(s1 & s2 & s3 ))

for x in finalArray:
    if ord(x[2]) < 91:
        total += ord(x[2])-38
    else:
        total += ord(x[2])-96

print(total)

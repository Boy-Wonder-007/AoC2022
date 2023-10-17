f = open("./info/5.txt", "r")

lines = f.read().splitlines()

count = 0

for x in lines:

    count += 1

    if len(x) < 1:
        continue
        
    if x[1] == "1":
        break

commands = lines[count+1:]
count -= 1

sortingArray = [[],[],[],[],[],[],[],[],[]]

while count > 0:
    count -= 1
    for x in range(int((len(lines[count])-2)/4)+1):
        sortingArray[x].append(lines[count][x*4+1])

count2 = 0
sortedArray = [[],[],[],[],[],[],[],[],[]]

for x in sortingArray:
    for y in x:
        if y != " ":
            sortedArray[count2].append(y)
    count2 += 1

count3 = 0

for x in commands:
    splits = x.split()
    amount = int(splits[1])
    start = int(splits[3])-1
    final = int(splits[5])-1
    lift = sortedArray[start][len(sortedArray[start])-amount:]
    #lift.reverse() #controls whether it is lifter 9000 or 9001
    for y in lift:
        sortedArray[final].append(y)
    sortedArray[start] = sortedArray[start][:len(sortedArray[start])-amount]

for x in sortedArray:
    print(x)
    

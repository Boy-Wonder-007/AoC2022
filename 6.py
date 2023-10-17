f = open("./info/6.txt", "r")

lines = f.read()

count = 0
tempArray = []

while count < len(lines):
    tempArray.append(lines[count])
    if len(tempArray) == 4:
        #print(tempArray)
        if len(set(tempArray)) == 4:
            print(count+1)
            break
        tempArray.pop(0)
    count += 1

count = 0
tempArray = []

while count < len(lines):
    tempArray.append(lines[count])
    if len(tempArray) == 14:
        #print(tempArray)
        if len(set(tempArray)) == 14:
            print(count+1)
            break
        tempArray.pop(0)
    count += 1
    

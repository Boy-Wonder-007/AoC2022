def readFile():
    f = open("./info/6.txt", "r")

    lines = f.read()
    return lines

def findPacket(lines, packetLen):
    count = 0
    tempArray = []

    while count < len(lines):
        tempArray.append(lines[count])
        if len(tempArray) == packetLen:
            #print(tempArray)
            if len(set(tempArray)) == packetLen:
                break
            tempArray.pop(0)
        count += 1
    return count+1

lines = readFile()

packet = findPacket(lines, 4)
message = findPacket(lines, 14)

print(packet, message)

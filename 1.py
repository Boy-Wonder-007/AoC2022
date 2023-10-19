def cleanText():
    f = open("./info/1.txt", "r")

    lines = f.readlines()
    correctLines = []

    for x in lines:
        correctLines.append(x.replace("\n", ""))
    correctLines.append("")
    return correctLines


def calcElfCarry(cleanText):
    total = 0
    highest = 0
    second = 0
    third = 0

    for x in cleanText:
        if x:
            total += int(x)
        else:
            if total > highest:
                third = second
                second = highest
                highest = total
            elif total > second:
                third = second
                second = total
            elif total > third:
                third = total
            total = 0
    return highest, highest+second+third

text = cleanText()
highest, total = calcElfCarry(text)

print(highest, total)

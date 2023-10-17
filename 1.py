f = open("./info/1.txt", "r")

lines = f.readlines()
correctLines = []
total = 0
highest = 0
second = 0
third = 0
for x in lines:
    correctLines.append(x.replace("\n", ""))
correctLines.append("")

for x in correctLines:
    if x != "":
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

print(highest, highest + second + third)


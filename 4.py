f = open("./info/4.txt", "r")

lines = f.read().splitlines()

count = 0

for x in lines:
    elf = x.split(",")
    elf1 = elf[0].split("-")
    elf2 = elf[1].split("-")
    elf1[0] = int(elf1[0])
    elf1[1] = int(elf1[1])
    elf2[0] = int(elf2[0])
    elf2[1] = int(elf2[1])

    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        count += 1
    elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
        count += 1

print(count)

count = 0

for y in lines:

    elf = y.split(",")
    elf1 = elf[0].split("-")
    elf2 = elf[1].split("-")
    elf1[0] = int(elf1[0])
    elf1[1] = int(elf1[1])
    elf2[0] = int(elf2[0])
    elf2[1] = int(elf2[1])

    if elf1[0] <= elf2[0] and elf1[1] >= elf2[0]:
        count += 1
    elif elf1[0] <= elf2[1] and elf1[1] >= elf2[1]:
        count += 1
    elif elf2[0] <= elf1[1] and elf2[1] >= elf1[1]:
        count += 1
    elif elf2[0] <= elf1[0] and elf2[1] >= elf1[0]:
        count += 1

print(count)

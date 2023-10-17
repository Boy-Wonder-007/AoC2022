pointArray = [[3, 0, 6],
              [6, 3, 0],
              [0, 6, 3]]

inpdict = {
    "A":0,
    "B":1,
    "C":2,
    "X":0,
    "Y":1,
    "Z":2
    }

score = 0

f = open("./info/2.txt", "r")

lines = f.read().splitlines()

for x in lines:
    score += pointArray[int(inpdict[x[2]])][int(inpdict[x[0]])]
    score += int(inpdict[x[2]]) + 1

print(score)

score = 0

for y in lines:
    if pointArray[0][int(inpdict[y[0]])] == int(inpdict[y[2]])*3:
        score += 1
    elif pointArray[1][int(inpdict[y[0]])] == int(inpdict[y[2]])*3:
        score += 2
    elif pointArray[2][int(inpdict[y[0]])] == int(inpdict[y[2]])*3:
        score += 3

    score += int(inpdict[y[2]])*3

print(score)




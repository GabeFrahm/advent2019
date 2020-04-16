file = open('input', 'r')
map = []
for i in file:
    map.append(i.strip())
def start(str):
    for i in map:
        if i.split(")")[0] == str:
            return i

listthing = []

def trace(str, target, templist=None):
    global listthing
    if templist == None:
        templist = []

    for i in map:
        if i.endswith(str): # START COUNTING
            if start(i.split(")")[0]).split(")")[0] == target:
                print(i)
                listthing = templist.copy()
                return 2
            else:
                print(i)
                templist.append(i.split(")")[0])
                return 1 + trace(i.split(")")[0], target, templist)

#totalY = 0
#totalS = 0

# START RUN
listY = []
listS = []

total = 0

for i in map:
    if i.split(")")[1] == "YOU":
        if i.split(")")[0] == "COM":
            total += 1
        else:
            total += trace(i.split(")")[0], "COM")
            listY = listthing.copy()
            break

for i in map:
    if i.split(")")[1] == "SAN":
        if i.split(")")[0] == "COM":
            total += 1
        else:
            total += trace(i.split(")")[0], "COM")
            listS = listthing.copy()
            break

newList = []

for i in listY:
    if i in listS:
        newList.append(i)

closest = newList[0]

print("####################################################################")
total = trace("YOU", closest)
print(total)
total += trace("SAN", closest)

print(total)

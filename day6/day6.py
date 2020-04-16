file = open('input', 'r')
map = []
for i in file:
    map.append(i.strip())
def start(str):
    for i in map:
        if i.split(")")[0] == str:
            return i
def trace(str):
    for i in map:
        if i.endswith(str): # START COUNTING
            print(i)
            if start(i.split(")")[0]).split(")")[0] == "COM":
                return 2
            else:
                return 1 + trace(i.split(")")[0])
total = 0
for i in map:
    if i.split(")")[0] == "COM":
        total += 1
    else:
        total += trace(i.split(")")[0])
print(total)

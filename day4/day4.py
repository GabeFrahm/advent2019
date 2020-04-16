range1 = 278384
range2 = 824795

validList = []

def c1(num):
    for i in range(len(str(num))):
        if str(num)[i] == str(num)[i - 1]:
            return True
    # AFTER FOR
    return False

def c2(num):
    for i in range(len(str(num))):
        if i != 0:
            if str(num)[i] < str(num)[i-1]:
                return False
    # AFTER FOR
    return True

def c1pt2(num):
    for i in range(len(str(num))):
        if(i != len(str(num)) - 1):
            if ((str(num)[i] == str(num)[i - 1]) and ((str(num)[i -2] != str(num)[i]) and (str(num)[i + 1] != str(num)[i]))):
                return True
        else:
            if ((str(num)[i] == str(num)[i - 1]) and (str(num)[i -2] != str(num)[i])):
                return True

    # AFTER FOR
    return False

for i in range(range1,range2):
    if c1pt2(i):
        if c2(i):
            validList.append(i)


print(len(validList))


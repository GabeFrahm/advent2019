opcodestr = """3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,34,224,101,-71,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1002,113,50,224,1001,224,-2550,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,13,50,225,102,7,187,224,1001,224,-224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1101,79,72,225,1101,42,42,225,1102,46,76,224,101,-3496,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,51,90,225,1101,11,91,225,1001,118,49,224,1001,224,-140,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,191,87,224,1001,224,-1218,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1,217,83,224,1001,224,-124,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,32,77,225,1101,29,80,225,101,93,58,224,1001,224,-143,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,45,69,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,344,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,419,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1108,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,509,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,1008,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226"""

# Formatting the list
code = list(map(int, opcodestr.split(",")))

# Parsing opcodes
def parseOp(pos):
    length = len(str(code[pos]))

    if length == 1:
        if code[pos] == 1:
            return addition(pos+1)
        elif code[pos] == 2:
            return multiplication(pos+1)
        elif code[pos] == 3:
            return getInput(pos+1)
        elif code[pos] == 4:
            return output(pos+1)
        elif code[pos] == 5:
            return jumpIfTrue(pos+1)
        elif code[pos] == 6:
            return jumpIfFalse(pos+1)
        elif code[pos] == 7:
            return lessThan(pos+1)
        elif code[pos] == 8:
            return equals(pos+1)

    elif length == 2:
        if code[pos] == 99:
            print(" - Finished. Diagnostic code above.")
            exit()

    elif length == 3:
        strcode = str(code[pos])
        mode1 = int(strcode[-3])

        if int(strcode[-1]) == 1:
            return addition(pos+1, mode1)
        elif int(strcode[-1]) == 2:
            return multiplication(pos+1, mode1)
        elif int(strcode[-1]) == 4:
            return output(pos+1, mode1)
        elif int(strcode[-1]) == 5:
            return jumpIfTrue(pos+1, mode1)
        elif int(strcode[-1]) == 6:
            return jumpIfFalse(pos+1, mode1)
        elif int(strcode[-1]) == 7:
            return lessThan(pos+1, mode1)
        elif int(strcode[-1]) == 8:
            return equals(pos+1, mode1)
    
    elif length == 4 or length == 5:
        strcode = str(code[pos])
        mode1 = int(strcode[-3])
        mode2 = int(strcode[-4])

        if int(strcode[-1]) == 1:
            return addition(pos+1, mode1, mode2)
        elif int(strcode[-1]) == 2:
            return multiplication(pos+1, mode1, mode2)
        elif int(strcode[-1]) == 5:
            return jumpIfTrue(pos+1, mode1, mode2)
        elif int(strcode[-1]) == 6:
            return jumpIfFalse(pos+1, mode1, mode2)
        elif int(strcode[-1]) == 7:
            return lessThan(pos+1, mode1, mode2)
        elif int(strcode[-1]) == 8:
            return equals(pos+1, mode1, mode2)
        

# OPCODE 1
def addition(p, m1=0, m2=0):
    p2 = p + 1
    p3 = p + 2
    # Setting num1 and 2 with ternaries and putting result in pos 'p3'
    code[code[p3]] = (code[code[p]] if m1 == 0 else code[p]) + (code[code[p2]] if m2 == 0 else code[p2])
    return i + 4

# OPCODE 2
def multiplication(p, m1=0, m2=0):
    p2 = p + 1
    p3 = p + 2
    # Setting num1 and 2 with ternaries and putting result in pos 'p3'
    code[code[p3]] = (code[code[p]] if m1 == 0 else code[p]) * (code[code[p2]] if m2 == 0 else code[p2])
    return i + 4

# OPCODE 3
def getInput(p):
    # Getting input and putting it in p1
    code[code[p]] = int(input("Enter Integer > "))
    return i + 2

# OPCODE 4
def output(p, m1=0):
    # Outputs p1
    if m1 == 0:
        print(f"Output:{code[code[p]]}")
    else:
        print(f"Output:{code[p]}")

    return i + 2

# OPCODE 5
def jumpIfTrue(p, m1=0, m2=0):
    p2 = p + 1
    if m1 == 0 and code[code[p]] != 0:
        if m2 == 0:
            return code[code[p2]]
        else:
            return code[p2]
    elif m1 == 1 and code[p] != 0:
        if m2 == 0:
            return code[code[p2]]
        else:
            return code[p2]
    else:
        return i + 3

# OPCODE 6
def jumpIfFalse(p, m1=0, m2=0):
    p2 = p + 1
    if m1 == 0 and code[code[p]] == 0:
        if m2 == 0:
            return code[p2]
        else:
            return code[p2]
    elif m1 == 1 and code[p] == 0:
        if m2 == 0:
            return code[code[p2]]
        else:
            return code[p2]
    else:
        return i + 3

# OPCODE 7
def lessThan(p, m1=0, m2=0):
    p2 = p + 1
    p3 = p + 2
    num1 = code[code[p]] if m1 == 0 else code[p]
    num2 = code[code[p2]] if m2 == 0 else code[p2]

    if num1 < num2:
        code[code[p3]] = 1
    else:
        code[code[p3]] = 0
    return i + 4

# OPCODE 8
def equals(p, m1=0, m2=0):
    p2 = p + 1
    p3 = p + 2
    num1 = code[code[p]] if m1 == 0 else code[p]
    num2 = code[code[p2]] if m2 == 0 else code[p2]

    if num1 == num2:
        code[code[p3]] = 1
    else:
        code[code[p3]] = 0
    return i + 4
    
# ---------------------
i = 0
while True:
    i = parseOp(i)

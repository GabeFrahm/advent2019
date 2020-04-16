opcodestr = """3,8,1001,8,10,8,105,1,0,0,21,46,63,76,97,118,199,280,361,442,99999,3,9,102,4,9,9,101,2,9,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,1002,9,5,9,1001,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99"""

num = ""
num2 = ""
times = 0
i = 0
final = "pp"

# Formatting the list
code = list(map(int, opcodestr.split(",")))

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
    global times
    if times == 0:
        code[code[p]] = num
    else:
        code[code[p]] = num2
    times += 1
    return i + 2

# OPCODE 4
def output(p, m1=0):
    # Outputs p1
    global final

    if m1 == 0:
        output = code[code[p]]
        print(f"Output:{output}")
        if output != 0:
            final = output
    else:
        output = code[p]
        print(f"Output:{output}")
        if output != 0:
            final = output

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
    
# OPCODE 99
def done(p):
    print("Finished... Diagnostic code above")
    return True
    
# Key dict
opcode = {
        1: addition,
        2: multiplication,
        3: getInput,
        4: output,
        5: jumpIfTrue,
        6: jumpIfFalse,
        7: lessThan,
        8: equals,
        99: done
}

# Parsing opcodes
def parseOp(pos):
    length = len(str(code[pos]))
    strcode = str(code[pos])

    if length == 1 or length == 2:
        return opcode[code[pos]](pos+1)

    elif length == 3:
        mode1 = int(strcode[-3])

        return opcode[int(str(code[pos])[-1])](pos+1, mode1)
    
    elif length == 4 or length == 5:
        mode1 = int(strcode[-3])
        mode2 = int(strcode[-4])
        
        return opcode[int(str(code[pos])[-1])](pos+1, mode1, mode2)
        
def run(thenum, prevoutput):
    global num, num2, i, code

    # RESET CODE
    code = list(map(int, opcodestr.split(",")))

    num = thenum
    num2 = prevoutput

    finished = False

    i = 0
    while finished == False:
        i = parseOp(i)
        if i == True:
            break
    return(final)

output1 = (run(4, 0))
output2 = (run(2, output1))
output3 = (run(1, output2))

print(output3)
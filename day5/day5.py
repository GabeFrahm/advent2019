opcodestr = """3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,34,224,101,-71,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1002,113,50,224,1001,224,-2550,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,13,50,225,102,7,187,224,1001,224,-224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1101,79,72,225,1101,42,42,225,1102,46,76,224,101,-3496,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,51,90,225,1101,11,91,225,1001,118,49,224,1001,224,-140,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,191,87,224,1001,224,-1218,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1,217,83,224,1001,224,-124,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,32,77,225,1101,29,80,225,101,93,58,224,1001,224,-143,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,45,69,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,344,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,419,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1108,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,509,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,1008,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226"""

# Format the list
code = opcodestr.split(",")
code = list(map(int, code))

def parsecode(start):
    # Check length
    tempint = 0

    if (code[start] == 1):    # OPCODE 1: Add
        tempint = code[code[start + 1]] + code[code[start + 2]]
        code[code[start + 3]] = tempint
        return 4

    elif code[start] == 2:  # OPCODE 2: Multiply
        tempint = code[code[start + 1]] * code[code[start + 2]]
        # Set tempint
        code[code[start + 3]] = tempint
        return 4

    elif code[start] == 3:  # OPCODE 3: Input
        userInput = int(input("Provide input > "))
        code[code[start + 1]] = userInput
        #print(code[225])
        return 2

    elif code[start] == 4:  # OPCODE 4: Output
        print("4 OUTPUT (mode 0; 1 dig):",code[code[start + 1]])
        #print("    - Current Index:", start)

        return 2
        
    elif code[start] == 99: # OPCODE 99: Stop
        print("Final after 99:",code[0])
        exit()
    
    # LONG OPCODES
    elif ((len(str(code[start])) == 4) or (len(str(code[start])) == 5)):
        mode1 = int(str(code[start])[len(str(code[start])) - 3])
        mode2 = int(str(code[start])[len(str(code[start])) - 4])
        # To test for errors. Will return an error if it's a string
        num1 = 0
        num2 = 0

        # ADDITION 
        if (int(str(code[start])[len(str(code[start])) - 1]) == 1):
            #print("OPCODE LONG ADDITION")
            #print("m1:",mode1)
            #print("m2:",mode2)
            if mode1 == 0:
                num1 = code[code[start + 1]]
            elif mode1 == 1:
                num1 = code[start + 1]
                #print("num1:",num1)

            if mode2 == 0:
                num2 = code[code[start + 2]]
            elif mode2 == 1:
                num2 = code[start + 2]
                #print("num2:",num2)
            
            tempint = num1 + num2
            #print("tempint:", tempint)
            code[code[start + 3]] = tempint
            #print("pos 225:", code[225])
            return 4

        # MULTIPLICATION
        elif (int(str(code[start])[len(str(code[start])) - 1]) == 2):
            if mode1 == 0:
                num1 = code[code[start + 1]]
            elif mode1 == 1:
                num1 = code[start + 1]

            if mode2 == 0:
                num2 = code[code[start + 2]]
            elif mode2 == 1:
                num2 = code[start + 2]
            
            tempint = num1 * num2
            code[code[start + 3]] = tempint
            return 4

    # 3 LONG OPCODE
    # (Opcode 3 is irrelevant as it's only asked at beginning)
    elif (len(str(code[start])) == 3):
        #print("3 LONG OPCODE")
        if (int(str(code[start])[-1]) == 4): # OPCODE 4
            #print("LONG OP 4")
            if(int(str(code[start])[0]) == 1):
                print("4 OUTPUT (mode 1):", code[start + 1])
            else:
                print("4 OUTPUT (mode 0):", code[code[start + 1]])
            return 2

        elif (int(str(code[start])[-1]) == 2): # OPCODE 2
            if(int(str(code[start])[0]) == 1):
                tempint = code[start + 1] * code[code[start + 2]]
                # Set tempint
                code[code[start + 3]] = tempint
            elif(int(str(code[start])[0]) == 0):
                tempint = code[code[start + 1]] * code[code[start + 2]]
                # Set tempint
                code[code[start + 3]] = tempint
            return 4

        elif (int(str(code[start])[-1]) == 1): # OPCODE 1
            if(int(str(code[start])[0]) == 1):
                tempint = code[start + 1] + code[code[start + 2]]
                # Set tempint
                code[code[start + 3]] = tempint
            elif(int(str(code[start])[0]) == 0):
                tempint = code[code[start + 1]] + code[code[start + 2]]
                # Set tempint
                code[code[start + 3]] = tempint
            return 4

i = 0
while True:
    iter = parsecode(i)
    #print("Current Value:",code[i])
    #print("Current Index:",iter)
    i = i + iter
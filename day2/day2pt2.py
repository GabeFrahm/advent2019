import random

opcodestr = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,123,127,1,127,6,0,99,2,14,0,0"
#code = opcodestr.split(",")
#code = list(map(int, code))

def parsecode():
    start = 0
    while True:
        tempint = 0

        if code[start] == 1:
            tempint = code[code[start + 1]] + code[code[start + 2]]
        elif code[start] == 2:
            tempint = code[code[start + 1]] * code[code[start + 2]]
        elif code[start] == 99:
            return(code[0])
            exit()
        code[code[start + 3]] = tempint
        start += 4

# Initializing 'a' (for attempts)
a = 0
while True:
    # Incrementing a
    a += 1
    
    # Initializing list 'code'
    code = opcodestr.split(",")
    code = list(map(int, code))

    # Generating two numbers
    int1 = random.randint(0,99)
    int2 = random.randint(0,99)

    # Inserting the numbers into the list
    code[1] = int1
    code[2] = int2

    # Checking if desired output
    if parsecode() == 19690720:
        # Formatting sutff
        if int1 < 10:
            int1 = "0" + str(int1)
        if int2 < 10:
            int2 = "0" + str(int2)

        # Print final output 
        print(f"The answer is: {str(int1)}{str(int2)}")
        print(f"that took {a} attempts... random gen may not be best")
        exit()

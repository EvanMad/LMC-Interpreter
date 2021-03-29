instructions = {
    "INP":901,
    "OUT":902,
    "ADD":1,
    "SUB":2,
    "STA":3,
    "LDA":5,
    "HLT":0,
}

debug = False
memory = {}

def run():
    pc = 0
    accumulator = 0
    i = 0
    data = open("test.asm", "r").readlines()
    lines = []
    for line in data:
        line = (line.rstrip())
        lineData = (line.split(" "))

        #get opcode and operand
        opcode = lineData[0]
        if len(lineData) == 2:
            operand = lineData[1]
        elif len(lineData) > 2 and lineData[1] == "DAT":
            memory[lineData[0]] = lineData[2]
        #So this is a loop thing
        elif len(lineData) > 2:
            memory[lineData[0]] = i
            opcode = lineData[1]
            operand = lineData[2]
        else:
            operand = None
        
        
        lines.append([opcode, operand])
        i+=1
    if debug:
        print(lines)

    while True:
        opcode = lines[pc][0]
        operand = lines[pc][1]
        pc+=1
        if debug:
            print("pc: {}, Instruction: {}".format(pc, opcode))

        #if opcode not in instructions:
            #print(lines[pc])

        if opcode == "INP":
            accumulator = int(input())
        if opcode == "STA":
            memory[operand] = accumulator
        if opcode == "LDA":
            accumulator = int(memory[operand])
        if opcode == "ADD":
            accumulator += int(memory[operand])
        if opcode == "SUB":
            accumulator -= int(memory[operand])
        if opcode == "OUT":
            print(accumulator)

        if opcode == "BRA":
            pc = memory[operand]
        if opcode == "BRP":
            if accumulator == 0 or accumulator > 0:
                pc = memory[operand]
                #pc = int(operand)
        if opcode == "BRZ":
            if accumulator == 0:
                pc = memory[operand]
        if opcode == "HLT":
            break
run()


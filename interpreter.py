import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--file", help="file to run")
parser.add_argument("--debug", help="debug info, 0 for no, 1 for yes")
args = parser.parse_args()

filepath = args.file
debug = int(args.debug)

valid_instructions = [
    "INP",
    "OUT",
    "ADD",
    "SUB",
    "STA",
    "LDA",
    "HLT",
    "DAT",
    "BRA",
    "BRZ",
    "BRP",
]


def run(filepath):
    memory = {} # Dict for storing variables and their values, quite handy really.
    pc = 0 #pc = programcounter
    accumulator = 0
    i = 0 #basically the linecount, it's only needed for the jump commands so it knows the instruction to jump to

    data = open(filepath, "r").readlines() #Get file
    instructions = []

    ##Read and process the lines into something more manageable, needs to be done first so we can do stuff like variable assignment at the end rather than beginning.
    for instruction in data:
        if instruction == "\n":
            continue
        instruction = (' '.join(instruction.split())) #Remove unholy whitespice at the beginning and end of lines. Allows for easier writing of code.
        instructionData = (instruction.split(" ")) ##Split the line up into it's parts

        #Adds ability to make inline comments, removes any words that begin with # from instruction
        for word in instructionData:
            if word.startswith("#"):
                instructionData.remove(word)

        # Prepare, might get a bit messy, probably a nicer way of doing this

        # get opcode and operand
        opcode = instructionData[0]

        # If it's not a standard instruction
        if opcode not in valid_instructions:
            #Assume (for now) that it's a loop setter
            memory[instructionData[0]] = i
            opcode = instructionData[1]

            if len(instructionData) == 2:
                operand = None
            # Sometimes instructions are formatted as ARSE DAT 0, which is perfectly acceptable apparently.
            elif instructionData[1] == "DAT":
                memory[instructionData[0]] = instructionData[2]
            # This checks if it's a standard loop setter with both an opcode and an operand, if so set them
            elif len(instructionData) == 3:
                operand = instructionData[2]

        #Standard opcode/operand duo
        elif len(instructionData) == 2:
            operand = instructionData[1]
        #So this checks if it's a DAT ARSE 0 variable assignemnt type, I've commented it out because it's not in the reference implimentation by higginson.
        #elif len(instructionData) > 2 and instructionData[1] == "DAT":
            #memory[instructionData[0]] = instructionData[2]
        else:
            operand = None
        
        instructions.append([opcode, operand])
        i += 1

    if debug:
        print(instructions)
        print(memory)

    #This is actually running the instructrions after they've been processed
    while True:
        opcode = instructions[pc][0]
        operand = instructions[pc][1]
        pc += 1
        if debug:
            print(memory)
        #Debug info
        if debug:
            print("pc: {}, Opcode: {}, Operand: {}".format(pc, opcode, operand))
        
        #Turns out python has no switch case, who knew?, this will do, it rhymes so it must be true.
        if opcode == "INP":
            accumulator = int(input())
            # This has also been commented out, some code examples use it, but the almighty higginson does not approve.
            #if operand is not None:
                #memory[operand] = accumulator
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
            #So by changing pc we can change the line of the assembly we're running, so here just jump to the position stored in the memory for that operand
            pc = memory[operand]
        if opcode == "BRP":
            if accumulator == 0 or accumulator > 0:
                pc = memory[operand]
        if opcode == "BRZ":
            if accumulator == 0:
                pc = memory[operand]

        if opcode == "HLT":
            break

if __name__ == "__main__":
    run(filepath)


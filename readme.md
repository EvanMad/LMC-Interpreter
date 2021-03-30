# LMC_Stuff
## Info
Some things I'm making based on [Peter Higginson's legendary demo computer demonstration](https://peterhigginson.co.uk/LMC/).
While instruction sets differ from source to source, [this instruction set from york university](https://www.yorku.ca/sychen/research/LMC/LMCInstructions.html) seems to be fully compatible with Higginson's demo, so It's what I based my code off.
I think at some point I'll write an emulator / toy compiler that read and writes straight from some kind of ROM, totally useless but should be fun.

## Interpreter
Pretty simple & easy python interpreter for text ASM files, so far works on basically every test I've put it through.
test.asm and sub.asm are provided as example files

Example programs taken from here https://www.yorku.ca/sychen/research/LMC/

Examples Below:

 `interpreter --file=triangular.asm --debug=0` (Squares your number)

 `interpreter --file=sub.asm --debug=1` (Subtracts your numbers)
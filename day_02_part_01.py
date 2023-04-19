# day_02_part_01.py
def intcode_program(intcode):
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if opcode == 99:
            break
        input1 = intcode[intcode[i+1]]
        input2 = intcode[intcode[i+2]]
        if opcode == 1:
            intcode[intcode[i+3]] = input1 + input2
        elif opcode == 2:
            intcode[intcode[i+3]] = input1 * input2
    return intcode

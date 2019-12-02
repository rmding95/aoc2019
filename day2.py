INPUT_FILENAME = "day2input.txt"
ADDITION_OPCODE = 1
MULTIPLICATION_OPCODE = 2
HALT_OPCODE = 99
STEP_SIZE = 4


def main():
    intcodes = parse_input()
    parse_intcodes(intcodes)
    print(intcodes)
    part2(intcodes)


def part2(intcodes):
    for noun in range(100):
        for verb in range(100):
            modified_intcodes = list(intcodes)
            modified_intcodes[1] = noun
            modified_intcodes[2] = verb
            parse_intcodes(modified_intcodes)
            if modified_intcodes[0] == 19690720:
                print(100 * noun + verb)


def parse_input():
    with open(INPUT_FILENAME) as f:
        s = f.read()
        return [int(x) for x in s.split(",")]


def parse_intcodes(intcodes):
    i = 0
    while i < len(intcodes):
        if intcodes[i] == HALT_OPCODE:
            return
        elif intcodes[i] == ADDITION_OPCODE:
            execute_opcode(intcodes, i, ADDITION_OPCODE)
        elif intcodes[i] == MULTIPLICATION_OPCODE:
            execute_opcode(intcodes, i, MULTIPLICATION_OPCODE)
        else:
            raise Exception("Encountered invald opcode: ", intcodes[i])
        i += STEP_SIZE


def execute_opcode(intcodes, start_index, opcode):
    assert start_index + 3 < len(intcodes), (start_index, intcodes)
    if opcode == ADDITION_OPCODE:
        intcodes[intcodes[start_index + 3]] = (
            intcodes[intcodes[start_index + 1]]
            + intcodes[intcodes[start_index + 2]]
        )
    else:
        intcodes[intcodes[start_index + 3]] = (
            intcodes[intcodes[start_index + 1]]
            * intcodes[intcodes[start_index + 2]]
        )


if __name__ == "__main__":
    main()

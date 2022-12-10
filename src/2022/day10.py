def part1(puzzle):
    cycle = 0
    register = 1
    signal_strengths = []
    total_cycles = find_total_cycles(puzzle)
    multiples = find_multiples(total_cycles)

    for instruction in puzzle:
        instruction = instruction.split(" ")
        if instruction[0] == "noop":
            cycle += 1
        else:
            for _ in range(2):
                cycle += 1
                if cycle in multiples:
                    signal_strengths.append(register * cycle)
            register = register + int(instruction[1])
    return sum(signal_strengths)


def part2(puzzle):
    program = []
    for cycle in range(40):
        sprite_position = [0, 1, 2]
        pixel = 0


def split_puzzle_multiple_40(puzzle):
    cycle = 0
    puzzle_by_cycle = []
    multiples_40 = find_multiples_40(146)
    for instruction in puzzle:
        circuit = []
        if instruction == "noop":
            circuit.append(instruction)
            cycle += 1
            if cycle in multiples_40:
                puzzle_by_cycle.append(circuit)
        else:
            circuit.append(instruction)
            for _ in range(2):
                cycle += 1
                if cycle in multiples_40:
                    puzzle_by_cycle.append(circuit)
    return puzzle_by_cycle


def find_total_cycles(puzzle):
    len_instruction_two_cycle = len([el for el in puzzle if el != "noop"])
    len_instruction_one_cycle = len([el for el in puzzle if el == "noop"])
    total_cycles = len_instruction_one_cycle + len_instruction_two_cycle * 2
    return total_cycles


def find_multiples(total_cycle):
    return [i for i in range(20, total_cycle, 40)]


def find_multiples_40(total_cycle):
    return [i for i in range(0, total_cycle, 40)]


if __name__ == "__main__":
    with open("2022/inputs/input10", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = split_puzzle_multiple_40(file.read().splitlines())
    print(f"The result is: {result}")

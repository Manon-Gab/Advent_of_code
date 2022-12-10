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


def find_total_cycles(puzzle):
    len_instruction_two_cycle = len([el for el in puzzle if el != "noop"])
    len_instruction_one_cycle = len([el for el in puzzle if el == "noop"])
    total_cycles = len_instruction_one_cycle + len_instruction_two_cycle * 2
    return total_cycles


def find_multiples(total_cycle):
    return [i for i in range(20, total_cycle, 40)]


if __name__ == "__main__":
    with open("2022/inputs/input10", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

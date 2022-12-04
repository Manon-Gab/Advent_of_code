def parse_puzzle(puzzle):
    list_of_sections = [pairs.split(",") for pairs in puzzle]
    list_of_assignments = []
    for pairs in list_of_sections:
        list_of_pairs = []
        for section in pairs:
            section = section.split("-")
            section = [int(el) for el in section]
            list_of_pairs.append(section)
        list_of_assignments.append(list_of_pairs)
    return list_of_assignments


def check_if_pair_contains_the_other(assignment):
    counter = 0
    # check if the first is in the second
    if assignment[1][0] <= assignment[0][0] <= assignment[1][-1]:
        if assignment[1][0] <= assignment[0][-1] <= assignment[1][-1]:
            counter = 1
    # check if the second is in the first
    if assignment[0][0] <= assignment[1][0] <= assignment[0][-1]:
        if assignment[0][0] <= assignment[1][-1] <= assignment[0][-1]:
            counter = 1
    return counter


def check_overlaps(assignment):
    counter = 0
    for id_section in range(assignment[0][0], assignment[0][-1] + 1):
        if assignment[1][0] <= id_section <= assignment[1][-1]:
            counter += 1
            break
    return counter


def part1(puzzle):
    list_of_sections = parse_puzzle(puzzle)
    list_counter = [
        check_if_pair_contains_the_other(section) for section in list_of_sections
    ]
    return sum(list_counter)


def part2(puzzle):
    list_of_sections = parse_puzzle(puzzle)
    overlapping_assignment = [check_overlaps(section) for section in list_of_sections]
    return sum(overlapping_assignment)


if __name__ == "__main__":
    with open("2022/inputs/input4", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

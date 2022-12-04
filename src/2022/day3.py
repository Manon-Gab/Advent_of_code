import itertools


def part1(puzzle):
    puzzle_compartments = [
        [item[: len(item) // 2], item[len(item) // 2 :]] for item in puzzle
    ]
    list_of_common_letters = [
        "".join(set(compartments[0]).intersection(compartments[1]))
        for compartments in puzzle_compartments
    ]
    list_of_priority = get_list_of_priority(list_of_common_letters)
    return sum(list_of_priority)


def convert_by_priority(letter):
    if letter.isupper():
        # 64 - 26 = 38
        priority = ord(letter) - 38
    else:
        priority = ord(letter) - 96
    return priority


def get_list_of_priority(list_of_common_letters):
    return [convert_by_priority(letter) for letter in list_of_common_letters]


def part2(puzzle):
    puzzle_group_by_three = [puzzle[i : i + 3] for i in range(0, len(puzzle), 3)]
    list_of_common_letters = [
        "".join(set(compartments[0]).intersection(compartments[1], compartments[2]))
        for compartments in puzzle_group_by_three
    ]
    list_of_priority = get_list_of_priority(list_of_common_letters)
    return sum(list_of_priority)


if __name__ == "__main__":
    with open("2022/inputs/input3", "r") as file:
    # with open("2022/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

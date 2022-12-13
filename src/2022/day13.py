def part1(puzzle):
    input = parse_input(puzzle)
    counter = 0
    for idx, pairs in enumerate(input):
        order = compare_list(pairs[0], pairs[1])
        if order:
            counter += idx + 1

    return counter


def compare_list(list_1, list_2):
    print(f"{list_1} {list_2}")

    if not list_1 and list_2:
        return True
    elif list_1 and not list_2:
        return False
    elif (
        list_1 and list_2 and isinstance(list_1[0], int) and isinstance(list_2[0], int)
    ):
        if list_1[0] == list_2[0]:
            return compare_list(list_1[1:], list_2[1:])
        else:
            return list_1[0] < list_2[0]
    elif list_1 and list_2 and isinstance(list_1[0], int):
        return compare_list([list_1], list_2)
    elif list_1 and list_2 and isinstance(list_2[0], int):
        return compare_list(list_1, [list_2])
    elif (
        list_1[0] == list_2[0]
        and isinstance(list_1[0], list)
        and isinstance(list_2[0], list)
    ):
        return compare_list(list_1[1:], list_2[1:])

    elif list_1 and list_2:
        return compare_list(list_1[0], list_2[0])


def parse_input(puzzle):

    new_puzzle = []
    sub_tab = []
    for idx, el in enumerate(puzzle):
        if el != "":
            sub_tab.append(eval(el))
        else:
            new_puzzle.append(sub_tab)
            sub_tab = []
    if sub_tab:
        new_puzzle.append(sub_tab)

    return new_puzzle


if __name__ == "__main__":
    with open("2022/inputs/input13", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

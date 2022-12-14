from functools import total_ordering


@total_ordering
class Packet:
    """Redefine sort() function (__lt__) for part 2."""

    def __init__(self, row):
        self.row = eval(row)

    def __eq__(self, other):
        return self.row == other.row

    def __lt__(self, other):
        return self.compare_list(self.row, other.row)

    @staticmethod
    def compare_list(list_1, list_2):
        """Compare two lists, examine each case."""
        # One empty list
        if not list_1 and list_2:
            return True
        elif list_1 and not list_2:
            return False
        # compare integer
        elif (
            list_1
            and list_2
            and isinstance(list_1[0], int)
            and isinstance(list_2[0], int)
        ):
            if list_1[0] == list_2[0]:
                return compare_list(list_1[1:], list_2[1:])
            else:
                return list_1[0] < list_2[0]
        # Compare list and integer, call the fonction taking the first element of the list.
        elif list_1 and list_2 and isinstance(list_1[0], int):
            return compare_list([list_1], list_2)
        elif list_1 and list_2 and isinstance(list_2[0], int):
            return compare_list(list_1, [list_2])
        # Compare list of list
        elif (
            list_1[0] == list_2[0]
            and isinstance(list_1[0], list)
            and isinstance(list_2[0], list)
        ):
            return compare_list(list_1[1:], list_2[1:])
        # compare 2 list not empty
        elif list_1 and list_2:
            return compare_list(list_1[0], list_2[0])


def part1(puzzle):
    input = parse_input_part1(puzzle)
    counter = 0
    for idx, pairs in enumerate(input):
        order = compare_list(pairs[0], pairs[1])
        if order:
            counter += idx + 1
    return counter


def part2(puzzle):
    puzzle.extend(["[[2]]", "[[6]]"])
    new_puzzle = parse_input_part2(puzzle)
    new_puzzle.sort()
    packets_list = [el.row for el in new_puzzle]
    idx_6 = packets_list.index([[6]]) + 1
    idx_2 = packets_list.index([[2]]) + 1
    return idx_6 * idx_2


def compare_list(list_1, list_2):
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
        list_1
        and list_2
        and list_1[0] == list_2[0]
        and isinstance(list_1[0], list)
        and isinstance(list_2[0], list)
    ):
        return compare_list(list_1[1:], list_2[1:])

    elif list_1 and list_2:
        return compare_list(list_1[0], list_2[0])


def parse_input_part1(puzzle):

    new_puzzle = []
    sub_tab = []
    for idx, el in enumerate(puzzle):
        if el != "":
            sub_tab.append(eval(el))
            new_puzzle.append(Packet(el))
        else:
            new_puzzle.append(sub_tab)
            sub_tab = []
    if sub_tab:
        new_puzzle.append(sub_tab)
    new_puzzle = [el.row for el in new_puzzle]
    return new_puzzle


def parse_input_part2(puzzle):

    new_puzzle = []
    for idx, el in enumerate(puzzle):
        if el != "":
            new_puzzle.append(Packet(el))
    return new_puzzle


if __name__ == "__main__":
    with open("2022/inputs/input13", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

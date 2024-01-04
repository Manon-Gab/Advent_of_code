def find_coord_symbol(puzzle):
    coord_symbol = []
    for y, line in enumerate(puzzle):
        for x, case in enumerate(line):
            if not case.isdigit() and case != ".":
                coord_symbol.append([x, y])
    return coord_symbol


def part1(puzzle):
    coord_symbol = find_coord_symbol(puzzle)
    print(coord_symbol)
    list_nb = []
    for y, line in enumerate(puzzle):
        nb = []
        for x, case in enumerate(line):
            coord_digit = [
                [x, y + 1],
                [x, y - 1],
                [x + 1, y + 1],
                [x + 1, y - 1],
                [x + 1, y],
                [x - 1, y - 1],
                [x - 1, y + 1],
                [x - 1, y],
            ]
            condition = not any(coord in coord_digit for coord in coord_symbol)
            for i in range(x + 1, len(line)):

                if case.isdigit() and line[i].isdigit() and condition:

                    nb.append(case)
                elif case.isdigit() and line[i] == "." and condition:
                    print(x, y)
                    nb.append(case)
                    nb.append("-")
                    list_nb.append(nb)
                    nb = []
                else:
                    nb = []

    print(list_nb)

    # list_numbers = "".join(nb).split("-")
    # numbers = [int(el) for el in list_numbers if el.isdigit()]
    # print(numbers)
    # list_nb.extend(numbers)

    return sum(list_nb)


if __name__ == "__main__":
    with open("2023/inputs/test_input", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

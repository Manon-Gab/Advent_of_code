MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

LIST_NB = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def part2(puzzle):
    list_calibation = []
    for lines in puzzle:
        list_nb = find_numbers(lines)
        if list_nb:
            line = replace_letters(lines, list_nb)
        else:
            line = lines
        list_nb = [el for el in line if el.isdigit()]
        print(int("".join([list_nb[0], list_nb[-1]])))
        list_calibation.append(int("".join([list_nb[0], list_nb[-1]])))

    return sum(list_calibation)


def part1(puzzle):
    list_calibation = []
    for line in puzzle:
        list_nb = [el for el in line if el.isdigit()]
        list_calibation.append(int("".join([list_nb[0], list_nb[-1]])))
    return sum(list_calibation)


# def replace_letters(line, res, i):
#     for key, value in MAPPING.items():
#         if key in line:
#             newline = line.replace(key, value)
#             res.append(newline)
#             replace_letters(newline, res, i)
#             return res[-1]


def replace_letters(line, list_nb):
    first = line.replace(list_nb[0], MAPPING[list_nb[0]])
    second = first.replace(list_nb[-1], MAPPING[list_nb[-1]])
    return second


def find_numbers(line):
    res = []
    for i in range(len(line)):
        if line[i:].startswith(tuple(LIST_NB)):
            if line[i : i + 5] in LIST_NB:
                res.append(line[i : i + 5])
            elif line[i : i + 4] in LIST_NB:
                res.append(line[i : i + 4])
            elif line[i : i + 3] in LIST_NB:
                res.append(line[i : i + 3])
    if len(res) > 2:
        res = [res[0], res[-1]]
    return res


if __name__ == "__main__":
    with open("2023/inputs/input1", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

# 53270

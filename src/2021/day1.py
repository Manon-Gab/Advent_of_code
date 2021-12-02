def part1(puzzle):
    puzzle = [int(el) for el in puzzle]
    count = 0
    for i in range(len(puzzle) - 1):
        if (puzzle[i]) < (puzzle[i + 1]):
            count = count + 1
    return count


def part2(puzzle):
    puzzle = [int(el) for el in puzzle]
    sum_tab = [
        puzzle[i] + puzzle[i + 1] + puzzle[i + 2] for i in range(len(puzzle) - 2)
    ]
    res = part1(sum_tab)
    return res


if __name__ == "__main__":
    with open("2021/inputs/input1", "r") as file:
        # with open("2021/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

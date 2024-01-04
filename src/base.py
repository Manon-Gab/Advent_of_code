def part1(puzzle):
    return puzzle


if __name__ == "__main__":
    with open("year/inputs/input_nb", "r") as file:
        # with open("year/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

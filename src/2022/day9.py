def part1(puzzle):
    return puzzle


if __name__ == "__main__":
    # with open("2022/inputs/input9", "r") as file:
    with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

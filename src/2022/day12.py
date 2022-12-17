from string import ascii_lowercase


def part1(puzzle):
    counter = 0
    previous_pos = search_letter_in_tab(puzzle, "E")[0]
    for letter in ascii_lowercase[::-1]:
        positions = search_letter_in_tab(puzzle, letter)
        for position in positions:
            if position in [
                (previous_pos[0] - 1, previous_pos[1]),
                (previous_pos[0] + 1, previous_pos[1]),
                (previous_pos[0], previous_pos[1] - 1),
                (previous_pos[0], previous_pos[1] + 1),
            ]:
                previous_pos = position
                counter += 1
            else:
                pass
                # Find the same letter as before
    return positions


def search_letter_in_tab(puzzle, character):
    """Find the coordinate of a letter."""
    return [
        (x, y)
        for x, row in enumerate(puzzle)
        for y, letter in enumerate(row)
        if letter == character
    ]


if __name__ == "__main__":
    # with open("2022/inputs/input12", "r") as file:
    with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

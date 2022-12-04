def part1(puzzle):
    mapping_player = {"X": 1, "Y": 2, "Z": 3}
    combination_round = {
        "A X": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
        "C Z": 3,
    }
    results_round = [
        (combination_round[game] + mapping_player[game[-1]]) for game in puzzle
    ]
    return sum(results_round)


def part2(puzzle):
    mapping_game = {
        "A X": "A Z",
        "A Y": "A X",
        "A Z": "A Y",
        "B X": "B X",
        "B Y": "B Y",
        "B Z": "B Z",
        "C X": "C Y",
        "C Y": "C Z",
        "C Z": "C X",
    }
    new_puzzle = [mapping_game[game] for game in puzzle]
    return part1(new_puzzle)


if __name__ == "__main__":
    with open("2022/inputs/input2", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

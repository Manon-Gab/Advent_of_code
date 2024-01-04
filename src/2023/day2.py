import json
import math

MAX_BAG = {"blue": 14, "red": 12, "green": 13}


def part1(puzzle):
    readable_input = parse_input(puzzle)
    possible_game = set(range(1, len(readable_input) + 1))
    for game, sets in readable_input.items():
        for set_game in sets:
            for color, max_nb in MAX_BAG.items():
                try:
                    if set_game[color] > max_nb:
                        possible_game.remove(int(game))
                except KeyError:
                    pass
    return sum(possible_game)


def part2(puzzle):
    readable_input = parse_input(puzzle)
    input_max = {}
    for game, sets in readable_input.items():
        input_max[game] = math.prod([el for el in find_max(sets).values()])
    return sum([el for el in input_max.values()])


def parse_input(puzzle):
    sets = {
        int(game.split(":")[0].split(" ")[-1]): game.split(":")[-1] for game in puzzle
    }
    for game, value in sets.items():
        sets[game] = [
            {el.split(" ")[-1]: int(el.split(" ")[1]) for el in line.split(",")}
            for line in value.split(";")
        ]
    return sets


def find_max(line):
    new = {"blue": [], "red": [], "green": []}
    for color in ["blue", "red", "green"]:
        for el in line:
            try:
                new[color].append(el[color])
            except KeyError:
                new[color].append(1)
        new[color] = max(new[color])
    return new


if __name__ == "__main__":
    with open("2023/inputs/input2", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
        # result = json.dumps(result, indent=4)
    print(f"The result is: {result}")

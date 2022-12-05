import csv


def part1(actions, stack_crates):
    for move in actions:
        for _ in range(move[0]):
            # -1 => list start at 0
            stack_crates[move[2] - 1].append(stack_crates[move[1] - 1][-1])
            del stack_crates[move[1] - 1][-1]
    return stack_crates


def part2(actions, stack_crates):
    for move in actions:
        len_stack_crates_to_move = len(stack_crates[move[1] - 1])
        stack_crates[move[2] - 1].extend(
            stack_crates[move[1] - 1][len_stack_crates_to_move - move[0] :]
        )
        del stack_crates[move[1] - 1][len_stack_crates_to_move - move[0] :]
    return stack_crates


def base_part(puzzle):
    actions = parse_move(puzzle)
    stack_crates = parse_stack_crates()
    stack_crates = part2(actions, stack_crates)
    letters = get_top_crate(stack_crates)
    word = "".join(letters)
    return word


def get_top_crate(stack_crates):
    top_end_list = [crate[-1] for crate in stack_crates]
    top_letters = [crate[1] for crate in top_end_list]
    return top_letters


def parse_move(puzzle):
    actions = [move.split(" ") for move in puzzle]
    int_actions = [[int(el) for el in lines if el.isdigit()] for lines in actions]
    return int_actions


def parse_stack_crates():
    with open("2022/inputs/input5", "r") as file:
        read_puzzle = file.readlines()
    input = list(csv.reader(read_puzzle, delimiter=" "))[:-1]
    for row in input:
        for crates in row:
            # 4 spaces corresponding at one empty crate
            if crates == "":
                first_index = row.index(crates)
                del row[first_index : first_index + 4]
                row.insert(first_index, "[]")
        # complete the row by empty list
        nb_elements_to_completed = 9 - len(row)
        if nb_elements_to_completed != 0:
            row.extend(["[]"] * nb_elements_to_completed)
    # transpose the list
    parse_input = list(map(list, zip(*input[::-1])))
    # remove empty crates
    parse_input = [[item for item in a if item != "[]"] for a in parse_input]
    return parse_input


if __name__ == "__main__":
    with open("2022/inputs/input5_move", "r") as file:
        result = base_part(file.read().splitlines())
    print(f"The result is: {result}")

def part1(puzzle):
    commands = ["forward", "up", "down"]
    commands_dict = {}
    for command in commands:
        command_list = [int(el.split()[1]) for el in puzzle if el.split()[0] == command]
        command_sum = sum(command_list)
        commands_dict[command] = command_sum
    depth = commands_dict["forward"] * (commands_dict["down"] - commands_dict["up"])
    return depth


def part2(puzzle):
    commands_list = [el.split() for el in puzzle]
    aim = 0
    horizon_pos = 0
    depth = 0
    for command in commands_list:
        if command[0] == "forward":
            horizon_pos = horizon_pos + int(command[1])
            depth = depth + (aim * int(command[1]))
        if command[0] == "down":
            aim = aim + int(command[1])
        if command[0] == "up":
            aim = aim - int(command[1])
    result = horizon_pos * depth
    return result


if __name__ == "__main__":
    with open("2021/inputs/input2", "r") as file:
        # with open("2021/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

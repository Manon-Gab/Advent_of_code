def create_filesystem(puzzle):
    size_directories = {}
    current_path = []
    for command in puzzle:
        if command[0] == "$":
            split_cmd = command.split(" ")
            if split_cmd[1] == "cd":
                if split_cmd[2] != "..":
                    path = split_cmd[2]
                    current_path.append(path)
                    join_current_path = "/".join(current_path)
                    size_directories[join_current_path] = []
                else:
                    current_path = current_path[:-1]

        else:
            split_cmd = command.split(" ")
            directories_to_add = [
                "/".join(current_path[: idx + 1]) for idx, el in enumerate(current_path)
            ]
            if split_cmd[0] != "dir":
                for dir in directories_to_add:
                    size_directories[dir].append(int(split_cmd[0]))

    return size_directories


def calcul_size(size):
    return {key: sum(value) for key, value in size.items()}


def part1(puzzle):
    filesystem = create_filesystem(puzzle)
    nested_size = calcul_size(filesystem)
    list_size_inf_1000 = [value for value in nested_size.values() if value < 100000]
    return sum(list_size_inf_1000)


if __name__ == "__main__":
    with open("2022/inputs/input7", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

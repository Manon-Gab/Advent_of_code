def part1(puzzle):
    rock_paths = parse_puzzle(puzzle)
    min_y, max_y, min_x, max_x = find_min_max(rock_paths)
    empty_scan = [["." for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    # add base part
    scan = drawing_rock(empty_scan, rock_paths)
    # complete rock path
    new_rock_paths = []
    for path in rock_paths:
        add_to_path = path
        for i in range(len(path[:-1])):
            coord_to_add = compare_two_coord(path[i], path[i + 1])
            if coord_to_add:
                add_to_path.extend(coord_to_add)
        new_rock_paths.append(add_to_path)

    scan = drawing_rock(scan, new_rock_paths)
    try:
        for _ in range(10000000):
            for x in range(len(scan) - 1):
                add_sand(scan, x, 500)
    except IndexError:
        pass
    counter = 0
    for row in scan:
        for unit in row:
            if unit == "o":
                counter += 1
    # for row in scan:
    #     print(row[490:515])
    return counter


def add_sand(scan, x, y):
    if scan[x + 1][y] == ".":
        return add_sand(scan, x + 1, y)

    # Left edge management
    elif y == 0 and scan[x + 1][y] != "." and scan[x + 1][y + 1] != ".":
        scan[x][y] = "o"
        return True

    elif scan[x + 1][y] != "." and scan[x + 1][y - 1] == ".":
        return add_sand(scan, x + 1, y - 1)

    # Right edge management
    elif y == len(scan[0]) and scan[x + 1][y - 1] != "." and scan[x + 1][y] != ".":
        scan[x][y] = "o"
        return True
    elif (
        scan[x + 1][y] != "."
        and scan[x + 1][y - 1] != "."
        and scan[x + 1][y + 1] == "."
    ):
        return add_sand(scan, x + 1, y + 1)
    elif (
        scan[x + 1][y] != "."
        and scan[x + 1][y - 1] != "."
        and scan[x + 1][y + 1] != "."
    ):
        scan[x][y] = "o"
        return True


def drawing_rock(scan, rock_paths):
    for path in rock_paths:
        for idx, coord in enumerate(path):
            scan[coord[1]][coord[0]] = "#"
    return scan


def parse_puzzle(puzzle):
    rock_paths = [
        [[int(el) for el in coord.split(",")] for coord in line]
        for line in [rock_path.split(" -> ") for rock_path in puzzle]
    ]
    return rock_paths


def find_min_max(rock_paths):
    min_y = min([coord[0] for row in rock_paths for coord in row])
    max_y = max([coord[0] for row in rock_paths for coord in row])
    min_x = min([coord[1] for row in rock_paths for coord in row])
    max_x = max([coord[1] for row in rock_paths for coord in row])
    return int(min_y), int(max_y), int(min_x), int(max_x)


def compare_two_coord(coord_1, coord_2):
    to_add = []
    if coord_1[0] == coord_2[0]:
        if coord_1[1] < coord_2[1]:
            for i in range(coord_1[1] + 1, coord_2[1]):
                to_add.append([coord_1[0], i])
        else:
            for i in range(coord_2[1] + 1, coord_1[1]):
                to_add.append([coord_1[0], i])

    else:
        if coord_1[0] < coord_2[0]:
            for i in range(coord_1[0] + 1, coord_2[0]):
                to_add.append([i, coord_1[1]])
        else:
            for i in range(coord_2[0] + 1, coord_1[0]):
                to_add.append([i, coord_1[1]])
    return to_add


if __name__ == "__main__":
    with open("2022/inputs/input14", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

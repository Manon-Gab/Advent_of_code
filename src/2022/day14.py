def part1(puzzle):
    rock_paths = parse_puzzle(puzzle)
    max_y, max_x = find_max(rock_paths)
    empty_scan = [["." for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    # complete rock path
    new_rock_paths = complete_rock_path(rock_paths)
    # drawing the scan
    scan = drawing_rock(empty_scan, new_rock_paths)
    # add the units of sand in the scan
    for _ in range(1000):
        for x in range(len(scan)):
            try:
                add_sand(scan, x, 500)
            except IndexError:
                break
            break
    counter = count_units_of_sand(scan)
    # for row in scan:
    #     print(row[478:])
    return counter


def parse_puzzle(puzzle):
    rock_paths = [
        [[int(el) for el in coord.split(",")] for coord in line]
        for line in [rock_path.split(" -> ") for rock_path in puzzle]
    ]
    return rock_paths


def find_max(rock_paths):
    max_y = max([coord[0] for row in rock_paths for coord in row])
    max_x = max([coord[1] for row in rock_paths for coord in row])
    return int(max_y), int(max_x)


def drawing_rock(scan, rock_paths):
    for path in rock_paths:
        for coord in path:
            scan[coord[1]][coord[0]] = "#"
    return scan


def complete_rock_path(rock_paths):
    """Complete the list of rock coord."""
    new_rock_paths = []
    for path in rock_paths:
        add_to_path = path
        for i in range(len(path[:-1])):
            coord_to_add = compare_two_coord(path[i], path[i + 1])
            if coord_to_add:
                add_to_path.extend(coord_to_add)
        new_rock_paths.append(add_to_path)
    return new_rock_paths


def add_sand(scan, x, y):
    # print(f"x is: {x}")
    if scan[x + 1][y] == ".":
        return add_sand(scan, x + 1, y)

    elif scan[x + 1][y] != "." and scan[x + 1][y - 1] == ".":
        return add_sand(scan, x + 1, y - 1)

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


def count_units_of_sand(scan):
    counter = 0
    for row in scan:
        for unit in row:
            if unit == "o":
                counter += 1
    return counter


if __name__ == "__main__":
    with open("2022/inputs/input14", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

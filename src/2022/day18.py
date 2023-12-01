def part1(puzzle):
    coordinates_tab = [[int(coord) for coord in coords.split(",")] for coords in puzzle]
    max_x, max_y, max_z = find_max(coordinates_tab)
    empty_grid_xy = [["." for _ in range(max_y)] for _ in range(max_x + 3)]
    print(empty_grid_xy)
    return coordinates_tab

def find_max(coordinates_tab):
    max_y = max([coord[0] for coord in coordinates_tab])
    max_x = max([coord[1] for coord in coordinates_tab])
    max_z = max([coord[2] for coord in coordinates_tab])
    return int(max_y), int(max_x), int(max_z)

def drawing_cube(coordinates_tab, empty_grid_xy):
    for path in rock_paths:
        for coord in path:
            scan[coord[1]][coord[0]] = "#"
    return scan

if __name__ == "__main__":
    # with open("2022/inputs/input18", "r") as file:
    with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

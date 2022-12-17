import re


def part1(puzzle):
    parse_input, max_coord, min_coord = pase_puzzle(puzzle)
    return parse_input


def pase_puzzle(puzzle):
    input = []
    max_coord = [0, 0]
    min_coord = [0, 0]
    for row in puzzle:
        position = {}
        signal = row.split("closest")
        sensor_x = re.search("x=(.+?),", signal[0])
        sensor_x = int(sensor_x.group(1))
        sensor_y = re.search("y=(.+?):", signal[0])
        sensor_y = int(sensor_y.group(1))
        beacon_x = re.search("x=(.+?),", signal[1])
        beacon_x = int(beacon_x.group(1))
        beacon_y = int(signal[1][signal[1].find("y=") + 2 :])

        position["S"] = [sensor_x, sensor_y]
        position["B"] = [beacon_x, beacon_y]
        for values in position.values():
            for i in [0, 1]:
                if values[i] > max_coord[i]:
                    max_coord[i] = values[i]
            for j in [0, 1]:
                if values[j] < min_coord[j]:
                    min_coord[j] = values[j]
        input.append(position)
    return input, max_coord, min_coord


if __name__ == "__main__":
    # with open("2022/inputs/input15", "r") as file:
    with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

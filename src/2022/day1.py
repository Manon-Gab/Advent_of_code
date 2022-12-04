def base_part(puzzle):
    idx_list = [idx - 1 for idx, val in enumerate(puzzle) if val == ""]
    size = len(puzzle)
    idx_start = [0] + [idx + 2 for idx in idx_list]
    idx_end = idx_list + ([size] if idx_list[-1] != size else [])
    start_end_idx = list(zip(idx_start, idx_end))
    calories_lists = [puzzle[i : j + 1] for i, j in start_end_idx]
    int_calories_lists = [
        [eval(i) for i in cal_by_elves] for cal_by_elves in calories_lists
    ]
    total_for_each = [sum(x) for x in int_calories_lists]
    return total_for_each


def part1(puzzle):
    total_calories = base_part(puzzle)
    return max(total_calories)


def part2(puzzle):
    total_calories = base_part(puzzle)
    third_max_cal = [
        total_calories.pop(total_calories.index(max(total_calories))) for _ in range(3)
    ]
    return sum(third_max_cal)


if __name__ == "__main__":
    with open("2022/inputs/input1", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

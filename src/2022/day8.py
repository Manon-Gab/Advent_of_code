def part1(puzzle):
    list_position = browse_line(puzzle)
    uniq_result = list(set(list_position))
    nb_trees = len(uniq_result)
    return nb_trees


def browse_line(puzzle):
    list_position = []

    # from left to right
    for pos_y, line in enumerate(puzzle):
        position_y = len(puzzle) - pos_y - 1
        position_x = 0
        list_position.extend(check_row_direct(line, position_y, position_x))

    # from right to left
    for pos_y, line in enumerate(puzzle):
        position_y = len(puzzle) - pos_y - 1
        position_x = len(puzzle[0]) - 1
        list_position.extend(check_row_invers(line, position_y, position_x))

    vertical_puzzle = revert_puzzle(puzzle)
    # from up to down
    for pos_x, line in enumerate(vertical_puzzle):
        position_y = len(puzzle) - 1
        position_x = pos_x
        list_position.extend(check_row_direct_vertical(line, position_y, position_x))

    # from down to up
    for pos_x, line in enumerate(vertical_puzzle):
        position_y = 0
        position_x = pos_x
        list_position.extend(check_row_invers_vertical(line, position_y, position_x))

    return list_position


def revert_puzzle(puzzle):
    vertical_puzzle = [[] for _ in range(len(puzzle[0]))]
    for idx, row in enumerate(puzzle):
        for i, el in enumerate(row):
            vertical_puzzle[i].append(el)
    vertical_puzzle = ["".join(tree) for tree in vertical_puzzle]
    return vertical_puzzle


def check_row_direct(row, pos_y, pos_x):
    list_tree = [(pos_x, pos_y)]
    max_h = max([int(tree) for tree in row])
    row = update_row(row, max_h)
    for idx, tree in enumerate(row[:-1]):
        if int(tree) < int(row[idx + 1]):
            tupple_position = (pos_x + (idx + 1), pos_y)
            list_tree.append(tupple_position)
        elif int(tree) == int(row[idx + 1]):
            continue
        else:
            break
    return list_tree


def check_row_invers(row, pos_y, pos_x):
    list_tree = [(pos_x, pos_y)]
    max_h = max([int(tree) for tree in row])
    row = update_row(row[::-1], max_h)
    for idx, tree in enumerate(row[:-1]):
        if int(tree) < int(row[idx + 1]):
            tupple_position = (pos_x - (idx + 1), pos_y)
            list_tree.append(tupple_position)
        elif int(tree) == int(row[idx + 1]):
            continue
        else:
            break
    return list_tree


def check_row_direct_vertical(row, pos_y, pos_x):
    list_tree = [(pos_x, pos_y)]
    max_h = max([int(tree) for tree in row])
    row = update_row(row, max_h)
    for idx, tree in enumerate(row[:-1]):
        if int(tree) < int(row[idx + 1]):
            tupple_position = (pos_x, pos_y - (idx + 1))
            list_tree.append(tupple_position)
        elif int(tree) == int(row[idx + 1]):
            continue
        else:
            break
    return list_tree


def check_row_invers_vertical(row, pos_y, pos_x):
    list_tree = [(pos_x, pos_y)]
    max_h = max([int(tree) for tree in row])
    row = update_row(row[::-1], max_h)
    for idx, tree in enumerate(row[:-1]):
        if int(tree) < int(row[idx + 1]):
            tupple_position = (pos_x, idx + 1)
            list_tree.append(tupple_position)
        elif int(tree) == int(row[idx + 1]):
            continue
        else:
            break
    return list_tree


def update_row(row, max_h):
    """
    Change smaller tree to continue if we haven't reached the max yet:
    30314573 become 33334573
    """
    for idx, tree in enumerate(row[:-1]):
        tree = row[idx]
        if int(row[idx + 1]) < int(tree) < max_h:
            temp_row = list(row)
            temp_row[idx + 1] = tree
            row = "".join(temp_row)
    return row


if __name__ == "__main__":
    with open("2022/inputs/input8", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

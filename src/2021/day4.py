def part1(puzzle):
    boards = get_boards(puzzle)
    list_draw = get_list_draw(puzzle)
    for nb_draw in list_draw:
        for board in boards:
            board = check_nb(board, nb_draw)
            status_h = check_if_win(board)
            vertical_board = transform_vertical(board)
            status_v = check_if_win(vertical_board)
            if status_h or status_v:
                sum_unmark = sum_unmarked(board)
                break
        else:
            continue
        break
    result = sum_unmark * int(nb_draw)
    return result


def transform_input(puzzle):
    size = len(puzzle)
    idx_list = [idx + 1 for idx, val in enumerate(puzzle) if val == ""]
    list_entry = [
        puzzle[i:j]
        for i, j in zip(
            [0] + idx_list, idx_list + ([size] if idx_list[-1] != size else [])
        )
    ]
    for el in list_entry:
        if "" in el:
            el.remove("")
    return list_entry


def get_list_draw(entry):
    list_draw = transform_input(entry)[0]
    list_draw = list_draw[0].split(",")
    return list_draw


def get_boards(entry):
    boards = transform_input(entry)[1:]
    new_boards = []
    for board in boards:
        new_board = []
        for row in board:
            new_row = row.split(" ")
            while "" in new_row:
                new_row.remove("")
            new_board.append(new_row)
        new_boards.append(new_board)
    return new_boards


def check_nb(board, nb):
    for line in board:
        if nb in line:
            index = line.index(nb)
            line[index] = int(nb)
    return board


def check_if_win(board):
    status = False
    for line in board:
        if all(isinstance(x, int) for x in line):
            status = True
            break
        else:
            continue
    return status


def transform_vertical(board):
    new_vertical_board = []
    for i in range(len(board)):
        new_line = []
        for el in board:
            new_line.append(el[i])
        new_vertical_board.append(new_line)
    print(new_vertical_board)
    return new_vertical_board


def sum_unmarked(board):
    sum_unmarked = 0
    for line in board:
        for el in line:
            if isinstance(el, str):
                sum_unmarked = sum_unmarked + int(el)
    return sum_unmarked


if __name__ == "__main__":
    # with open("2021/inputs/test_input", "r") as file:
    with open("2021/inputs/input4", "r") as file:
        result = part1(file.read().split("\n"))
    print(f"The result is: {result}")

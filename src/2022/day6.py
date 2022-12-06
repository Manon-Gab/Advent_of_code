def base_part(puzzle, nb_characters):
    size = len(puzzle)
    for i in range(size - (nb_characters - 1)):
        packet = [letter for letter in puzzle[i : i + nb_characters]]
        if len(set(packet)) == nb_characters:
            # number of loop + number of characters by packet
            index = i + nb_characters
            break
    return index


if __name__ == "__main__":
    with open("2022/inputs/input6", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = base_part(file.read(), 14)
    print(f"The result is: {result}")

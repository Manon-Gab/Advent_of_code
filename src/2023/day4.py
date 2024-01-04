def part1(puzzle):
    list_card_value = []
    for card in puzzle:
        count_win = 0
        numbers = card.split(":")[1]
        wining_nb = [int(num) for num in (numbers.split("|")[0]).split()]
        your_nb = [int(num) for num in (numbers.split("|")[1]).split()]
        for nb in your_nb:
            if nb in wining_nb:
                count_win += 1
        if count_win > 0:
            card_value = 1
            for _ in range(count_win - 1):
                card_value *= 2
        else:
            card_value = 0
        list_card_value.append(card_value)
    return sum(list_card_value)


def part2(puzzle):
    list_card_numbers = []
    for line in puzzle:
        card_index = int((line.split(":")[0]).split()[1])
        list_card_numbers.append(card_index)
        numbers = line.split(":")[1]
        wining_nb = [int(num) for num in (numbers.split("|")[0]).split()]
        your_nb = [int(num) for num in (numbers.split("|")[1]).split()]
        count_win = 0
        for nb in your_nb:
            if nb in wining_nb:
                count_win += 1
        for _ in range(list_card_numbers.count(card_index)):
            for i in range(card_index + 1, card_index + count_win + 1):
                list_card_numbers.append(i)
    return len(list_card_numbers)


if __name__ == "__main__":
    with open("2023/inputs/input4", "r") as file:
        # with open("2023/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

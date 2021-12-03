def part1(puzzle):
    size = len(puzzle[0])
    gamma_rate = []
    epsilon_rate = []
    for diag in range(size):
        list_numbers = [int(el[diag]) for el in puzzle]
        didi = {list_numbers.count(1): 1, list_numbers.count(0): 0}
        gamma_rate.append(didi[max(didi)])
        epsilon_rate.append(didi[min(didi)])
    decimal_gamma = int("".join(map(str, gamma_rate)), 2)
    decimal_epsilon = int("".join(map(str, epsilon_rate)), 2)
    result = decimal_gamma * decimal_epsilon
    return result


def part2(puzzle):
    life_support_rating = {}
    list_of_numbers = puzzle
    for rate_type in ["oxygen", "CO2"]:
        pos = 0
        while len(list_of_numbers) > 1:
            new_list = find_bit(list_of_numbers, pos, rate_type)
            list_of_numbers = new_list
            pos += 1
        decimal = int("".join(map(str, new_list)), 2)
        list_of_numbers = puzzle
        life_support_rating[rate_type] = decimal
    result = life_support_rating["oxygen"] * life_support_rating["CO2"]
    return result


def find_bit(list_nb, pos, type_rate):
    rate_type = {"oxygen": [1, max], "CO2": [0, min]}
    list_numbers = [int(el[pos]) for el in list_nb]
    if list_numbers.count(1) == list_numbers.count(0):
        didi = {list_numbers.count(rate_type[type_rate][0]): rate_type[type_rate][0]}
    else:
        didi = {list_numbers.count(1): 1, list_numbers.count(0): 0}
    new_list = [
        el for el in list_nb if int(el[pos]) == didi[rate_type[type_rate][1](didi)]
    ]
    return new_list


if __name__ == "__main__":
    with open("2021/inputs/input3", "r") as file:
        # with open("2021/inputs/test_input", "r") as file:
        result = part2(file.read().splitlines())
    print(f"The result is: {result}")

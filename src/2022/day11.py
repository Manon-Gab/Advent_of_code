from itertools import groupby


def part1(puzzle):
    monkeys_list = parse_input(puzzle)
    parse_monkeys_list = parse_monkey(monkeys_list)
    inspected_items = {f"Monkey {i}": 0 for i in range(len(parse_monkeys_list))}
    for _ in range(20):
        for monkey, turn in enumerate(parse_monkeys_list):
            key = turn[str(monkey)]
            for item in key["items"]:
                # calculate worry level
                try:
                    eval(key["operation"][1])
                    new = f"{item} {key['operation'][0]} {key['operation'][1]}"
                except NameError:
                    new = f"{item} {key['operation'][0]} {item}"
                # Monkey gets bored with item
                worry_level = int(eval(new) / 3)
                # Count the number of times each monkey inspects items
                inspected_items[f"Monkey {monkey}"] += 1
                # send items
                if worry_level % key["div"] == 0:
                    parse_monkeys_list[int(key["true"])][key["true"]]["items"].append(
                        worry_level
                    )
                else:
                    parse_monkeys_list[int(key["false"])][key["false"]]["items"].append(
                        worry_level
                    )
            key["items"] = []
    # Find the 2 maximums
    monkey_business = find_max(inspected_items)
    result = monkey_business[0] * monkey_business[1]
    return result


def parse_monkey(monkeys_list):
    parse_monkeys_list = []
    for monkey, turn in enumerate(monkeys_list):
        key = f"{monkey}"
        monkey_dict = {key: {}}
        items = turn[f"Monkey {monkey}:"]["  Starting items"]
        monkey_dict[key]["items"] = [int(item) for item in items.split(", ")]
        monkey_dict[key]["operation"] = (
            turn[f"Monkey {monkey}:"]["  Operation"].split("old ")[1].split(" ")
        )
        monkey_dict[key]["div"] = int(
            turn[f"Monkey {monkey}:"]["  Test"].split("by ")[1]
        )
        monkey_dict[key]["true"] = turn[f"Monkey {monkey}:"]["    If true"].split(
            "monkey "
        )[1]
        monkey_dict[key]["false"] = turn[f"Monkey {monkey}:"]["    If false"].split(
            "monkey "
        )[1]
        parse_monkeys_list.append(monkey_dict)
    return parse_monkeys_list


def parse_input(puzzle):
    list_by_monkey = [
        list(group) for key, group in groupby(puzzle, key=lambda x: x == "") if not key
    ]
    monkeys_notes_list = []
    for monkey_notes in list_by_monkey:
        monkey_notes_dict = {monkey_notes[0]: {}}
        for notes in monkey_notes[1:]:
            notes = notes.split(":")
            monkey_notes_dict[monkey_notes[0]][notes[0]] = notes[1]
        monkeys_notes_list.append(monkey_notes_dict)
    return monkeys_notes_list


def find_max(inspected_items):
    monkey_business = []
    list_inspected_items = [values for values in inspected_items.values()]
    for _ in range(2):
        max_item = max(list_inspected_items)
        monkey_business.append(max_item)
        list_inspected_items.remove(max_item)
    return monkey_business


if __name__ == "__main__":
    with open("2022/inputs/input11", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = part1(file.read().splitlines())
    print(f"The result is: {result}")

filesystem = {}


def parse_input(puzzle, filesystem):
    # idx_command = [command[0] for command in enumerate(puzzle) if not command[1].startswith("$")]
    # lili = [idx_command[0]]
    # for i in range(len(idx_command)-1):
    #     if idx_command[i] + 1 == idx_command[i+1]:
    #         continue
    #     else:
    #         lili.append(idx_command[i+1])
    # print(lili)
    # for command in puzzle:
    #     if command.startswith("$ cd "):
    #         split_command = command.split("$ cd ")
    #         if split_command[1] != "..":
    #             filesystem[split_command[1]] =

    current_path = None
    new = {}
    for i, command in enumerate(puzzle):
        if command.startswith("$ cd "):
            split_command = command.split("$ cd ")
            current_path = split_command[1]
            new[split_command[1]] = []
            # start at i+2 because i is cd line, and i +1 is ls line
            for commandf in puzzle[i + 2 :]:
                if not commandf.startswith("$"):
                    new[split_command[1]].append(commandf)
                else:
                    break

    print(new)
    folder = {i: new[i] for i in new if i != "/"}
    res = test(new["/"], folder)
    print(res)
    result = transform_int(res)
    print(result)
    summ = calcul_total(result, [])
    res = sum(get_minus(summ))
    return res


def test(base, new):

    for i, el in enumerate(base):
        print(el)
        if el.startswith("dir"):
            direc = el.split(" ")
            base.insert(i, test(new[direc[1]], new))
            base.remove(el)
    return base


def transform_int(lili):
    for i, el in enumerate(lili):
        if isinstance(el, str):
            red = el.split(" ")
            lili.insert(i, int(red[0]))
            lili.remove(el)
        elif isinstance(el, list):
            transform_int(el)
    return lili


def nested_sum(L):
    total = 0
    for i in L:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total


def kjfbvkej(tot):
    list_inf = []
    total = nested_sum(tot)
    if total > 10000:
        for el in tot:
            if isinstance(el, list):
                total = kjfbvkej(el)
    else:
        list_inf.append(total)
        print(total)
    return list_inf


def calcul_total(result, list_inf):
    for el in result:
        print(el)
        if isinstance(el, list):
            print(nested_sum(el))
            list_inf.append(nested_sum(el))
            calcul_total(el, list_inf)
        # else:
        #     list_inf.append(el)
    return list_inf


def get_minus(list_inf):
    final_list = [el for el in list_inf if el < 100000]
    print(final_list)
    return final_list


# def recusive(base, new):
#     print(f"new is {new}")
#     print(f"base is {base}")
#     print("_____")
#     new_base = {}
#     for k, v in base.items():
#         new_base[k] = {}
#         if any(value.startswith("dir") for value in v):
#             for value in v:
#                 if value.startswith("dir"):
#                     directori = value.split(" ")
#                     new_base[k][directori[1]] = new[directori[1]]
#                     # recusive(new_base, new)
#                     # print(new_base) = {'/': {'a': ['dir e', '29116 f', '2557 g', '62596 h.lst']}}
#                 else:
#                     files = value.split(" ")
#                     new_base[k][files[0]] = files[1]
#                 new_base[k] = recusive(new_base[k], new)
#
#             print(new_base)
#         else:
#             new_base[k] = v
# result = new_base

#
# print("---------")
# return new_base


if __name__ == "__main__":
    with open("2022/inputs/input7", "r") as file:
        # with open("2022/inputs/test_input", "r") as file:
        result = parse_input(file.read().splitlines(), filesystem)
    print(f"The result is: {result}")

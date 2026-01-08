def sum_num(* args):
    total = 0

    for value in args:
        if isinstance(value, (int, float)):
            total += value
    return total

result = sum_num(10, 5.5, "hello", None, 3, True)
print(result)


def add_num(* args):
    total = 0

    for value in args:
        if type(value) == (int or float):
            total += value
    return total

results = add_num(10, 5.5, "hello", None, 3, True, 78)
print(results)


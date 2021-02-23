def for_else_check_odd_num(n: int):
    for i in range(n):
        if i == n / 2:
            break
    else:
        return True


def incorrect_default_list_value(a, li=[]):
    li.append(a)
    return li


def correct_default_list_value(a, li=None):
    if li is None:
        li = []
    li.append(a)
    return li

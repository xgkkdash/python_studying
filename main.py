def for_else_check_odd_num(n: int):
    for i in range(n):
        if i == n / 2:
            break
    else:
        return True

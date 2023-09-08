def reverse(x: int) -> int:
    if x == 0:
        return 0
    rev_num = ""
    if x < 0:
        num = -x
    else:
        num = x

    while num != 0:
        rev_num += str(num % 10)
        num = num // 10

    rev_num = (rev_num)

    if x < 0:
        rev_num = -rev_num

    return rev_num


print(reverse(2**31 - 1))

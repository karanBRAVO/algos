def addBinary(a: str, b: str) -> str:
    res = int(binaryTOdecimal(a)) + int(binaryTOdecimal(b))
    return str(decimalTObinary(str(res)))


def binaryTOdecimal(b_num: str) -> str:
    res = 0
    for i in range(0, len(b_num)):
        res += (2 ** i) * (int)(b_num[len(b_num) - (i + 1)])
    return str(res)


def decimalTObinary(d_num: str) -> str:
    base = 2
    rem = ""
    quo = int(d_num)
    while quo != 0:
        rem += str(quo % base)
        quo = quo // base
    res = ""
    for ele_index in range(0, len(rem)):
        res += rem[len(rem) - (ele_index + 1)]
    if len(res) > 0:
        return res
    else:
        return "0"


a = "0"
b = "0"
print(addBinary(a, b))
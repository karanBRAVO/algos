def countBits(n: int) -> list:
    ans_arr = []
    for i in range(0, n + 1, 1):
        bin_i = convert_to_binary(i)
        ans = count_1s(bin_i)
        ans_arr.append(ans)
    return ans_arr


def count_1s(num: str) -> str:
    count = 0
    for ele in num:
        if ele == "1":
            count += 1
    return count


def convert_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    binary_num = ""
    quo = n
    while quo > 0:
        rem = quo % 2
        quo = quo // 2
        binary_num  = str(rem) + binary_num
    return binary_num


n = int(input("Enter the number: "))
print(countBits(n))

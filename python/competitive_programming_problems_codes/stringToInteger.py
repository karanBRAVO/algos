def myAtoi(s: str) -> int:
    sign = ""
    whiteSpaces = " "
    number = ""
    char = ""

    for ele in s:
        if char == "":
            if ele == whiteSpaces:
                continue
        else:
            if ele == whiteSpaces or ele < "0" or ele > "9":
                break
            
        if sign == "":
            if ele == "-":
                sign = "-"
            else:
                sign = "+"
        
        char += ele

        if ele >= "0" and ele <= "9":
            if char[len(char) - 1: ] < "0" or char[len(char) - 1: ] > "9" and char[len(char) - 1: ] != ".":
                break
            number += str(ele)
        if ele == ".":
            number += ele

    if number == "":
        number = 0
    else:
        try:
            number = int(number)
        except ValueError:
            number = int(float(number))
    if sign == "-":
        number = number * -1

    if int(number) > 2 ** 31 - 1:
        return (2 ** 31 - 1)
    elif int(number) < - 2 ** 31:
        return (-(2 ** 31))
    else:
        return number


print(myAtoi("  -42"))

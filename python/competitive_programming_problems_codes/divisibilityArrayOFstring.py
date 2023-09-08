def divisibilityArray(word: str, m: int) -> list:
    div_arr = []
    rem = ""

    for i in range(0, len(word)):
        num = str(rem) + word[i]

        rem = int(num) % m

        if rem == 0:
            div_arr.append(1)
        else:
            div_arr.append(0)

    return div_arr


word = "1010"
m = 10

print(divisibilityArray(word, m))
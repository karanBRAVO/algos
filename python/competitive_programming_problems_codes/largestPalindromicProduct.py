testCases = int(input("~ Enter the test cases: "))


def checkPalindrome(n: int) -> bool:
    number_str = str(n)
    length = len(number_str)
    isPalindrome = True

    if length % 2 != 0:
        length -= 1

    i = 0
    while i < length / 2:
        if number_str[i] != number_str[len(number_str) - (i + 1)]:
            isPalindrome = False
            break
        i += 1

    return isPalindrome


def findProduct(n: int) -> int:
    palindrome = 0

    for i in range(101, 1000):
        for j in range(i, 1000):
            product = i * j
            if product > n or product <= palindrome:
                continue
            if checkPalindrome(product):
                palindrome = product

    return palindrome


for i in range(0, testCases):
    number = int(input("~ Enter the number(101101-1000000): "))
    print(
        f"largest palindrome less than and including {number} is {findProduct(number)}")

testCases = int(input("~ Enter the test cases: "))


def factorial(n):
    fact = 1
    for i in range(2, n + 1, 1):
        fact *= i
    return fact


for i in range(testCases):
    number = int(input("~ Enter the number: "))
    fact = str(factorial(number))
    sumDigits = 0
    for j in range(0, len(fact)):
        sumDigits += int(fact[j])
    print(f"Sum of digits of {number}! is {sumDigits}")
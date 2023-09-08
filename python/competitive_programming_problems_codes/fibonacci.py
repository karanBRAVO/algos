def fib(n: int) -> int:
    a = 0
    if n == 0:
        return a
    b = 1
    index = 2
    while index <= n:
        temp = b
        b = a + b
        a = temp
        index += 1
    return b


n = int(input("Enter the number: "))
print(fib(n=n))

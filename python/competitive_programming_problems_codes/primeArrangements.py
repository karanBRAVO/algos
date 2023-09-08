# Number of permutations such that prime number are at prime indices
# Prime numbers are in range 1 - n


def numPrimeArrangements(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    P = primeNumberCount(n)
    N = n - P
    return (factorial(N) * factorial(P)) % (10 ** 9 + 7)


def primeNumberCount(end: int) -> int:
    count = 2
    for i in range(5, end + 1, 2):
        if checkPrime(i):
            count += 1
    return count


def checkPrime(num: int) -> bool:
    i = 2
    while i <= num ** 0.5:
        if num % i == 0:
            return False
        i += 1
    return True


def factorial(n: int) -> int:
    fact = 1
    for i in range(2, n + 1, 1):
        fact *= i
    return fact


n = int(input("Enter the number: "))
print(numPrimeArrangements(n=n))

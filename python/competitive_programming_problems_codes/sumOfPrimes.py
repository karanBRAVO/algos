# pending -> optimal solution

testCases = int(input("~ Enter test cases: "))


def checkPrime(num):
    i = 2
    isFound = True
    while i <= num ** 0.5:
        if num % i == 0:
            isFound = False
            break
        i += 1
    return isFound


def sumOfPrimes(n):
    num = 2
    sumEle = 0 

    while num <= n:
        if checkPrime(num):
            sumEle += num

        if num >= 3:
            num += 2
        else:
            num += 1

    return sumEle


for i in range(0, testCases):
    number = int(input("~ Enter the number: "))
    if number > 1:
        print("Sum = ", sumOfPrimes(number))
    else:
        print("Sum = 0")
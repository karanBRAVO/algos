testCases = int(input("~ Enter the test cases: "))


# a, b, c -> Natural numbers
# a < b < c
def checkPythagoreanTriplet(a: int, b: int, c: int) -> bool:
    if (a ** 2) + (b ** 2) == (c ** 2):
        return True
    else:
        return False


def findTriplets(n) -> int:
    prod_arr = []

    for i in range(2, n  // 3, 1):
        for j in range(i + 1, n - (i + 1) - 1, 1):
            k = n - (i + j)
            if i != j and j != k and k != i:
                if checkPythagoreanTriplet(i, j, k):
                    prod_arr.append(i * j * k)

    if len(prod_arr) > 0:
        return max(prod_arr)
    else:
        return -1


for i in range(testCases):
    number = int(input("~ Enter the number: "))
    print(
        f"The product of pythagorean triplet whose sum is {number} is {findTriplets(number)}")

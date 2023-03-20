# T(n + 3) = T(n) + T(n + 1) + T(n + 2)  for n >= 0
def tribonacci(n: int) -> int:
    a = 0
    b = 1
    c = 1
    if n == 0: return a
    elif n == 1: return b
    elif n == 2: return c
    else:
        arr = [[f"T-{0}", a], [f"T-{1}", b], [f"T-{2}", c]]
        for i in range(0, n - 3 + 1, 1):
            arr.append([f"T-{i + 3}", a + b + c])
            temp1 = c
            temp2 = b
            c = a + b + c
            b = temp1
            a = temp2
        print(arr)
    return arr[len(arr) - 1][1]


n = int(input("Enter the value of n: "))
print(tribonacci(n))

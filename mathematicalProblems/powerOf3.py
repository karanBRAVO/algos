def isPowerOfThree(n: int) -> bool:
    if n < 0:
        return False
    elif n == 1:
        return True
    else:
        n_str = str(n)
        s = 0
        for i in n_str:
            s += int(i)
        if s % 3 != 0:
            return False
        else:
            power_3 = 3
            while power_3 < n:
                power_3 *= 3
            if power_3 == n:
                return True
            else:
                return False


n = int(input("Enter the number: "))
print(isPowerOfThree(n))

# 0 -> red | 1 -> white | 2 -> blue
# sort the input array such that all same colors are adjacent


def sortColorsFunc(arr: list) -> list:
    i = 1
    while i < len(arr):
        val = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > val:
                arr[j+1] = arr[j]
                arr[j] = val
            j -= 1
        i += 1
    return arr


arr = [int(x) for x in input().split()]
print(sortColorsFunc(arr))

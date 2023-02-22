g_arr = [10, 23, 34, 45, 56, 8, 56, 2, 1, 11]


def linearSearch(arr, length:int, targetVal:int) -> int:
    for i in range(0, length):
        if arr[i] == targetVal:
            return i
    
    return -1


if __name__ == "__main__":
    target = int(input("~ Enter the target: "))
    print(f"Target is at index {linearSearch(g_arr, len(g_arr), target)}")
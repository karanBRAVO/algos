g_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binarySearch(arr, start, end, targetVal):
    if start > end:
        return -1

    middle = (start + end) // 2

    if targetVal == arr[middle]:
        return middle
    elif targetVal < arr[middle]:
        end = middle - 1
        return binarySearch(arr, start, end, targetVal)
    elif targetVal > arr[middle]:
        start = middle + 1
        return binarySearch(arr, start, end, targetVal)


if __name__ == "__main__":
    target = int(input("~ Enter the Target: "))
    print(f"Target is at index {binarySearch(g_arr, 0, len(g_arr) - 1, target)}")
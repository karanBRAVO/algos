g_arr = [10, 1, 34, 8, 90, 30, 20, 11, 3, 2]


def quickSort(arr, length, pivot):
    if length <= 1:
        return

    ele = arr[pivot]
    leftArr = []
    rightArr = []

    for i in range(pivot):
        if arr[i] < ele:
            leftArr.append(arr[i])
        else:
            rightArr.append(arr[i])

    quickSort(leftArr, len(leftArr), len(leftArr) - 1)
    quickSort(rightArr, len(rightArr), len(rightArr) - 1)

    arr.clear()
    arr.extend(leftArr)
    arr.append(ele)
    arr.extend(rightArr)


if __name__ == "__main__":
    print("------ Initial arr ------")
    print(g_arr)
    quickSort(g_arr, len(g_arr), len(g_arr) - 1)
    print("------ Final arr ------")
    print(g_arr)

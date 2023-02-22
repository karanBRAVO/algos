g_arr = [10, 1, 34, 8, 90, 30, 20, 11, 3, 2]


def merge(oldArr, oldArr_length, leftArr, leftArr_length, rightArr, rightArr_length):
    i = 0
    j = 0
    k = 0

    while i < leftArr_length and j < rightArr_length and k < oldArr_length:
        if leftArr[i] > rightArr[j]:
            oldArr[k] = rightArr[j]
            j += 1
        else:
            oldArr[k] = leftArr[i]
            i += 1
        k += 1
    while i < leftArr_length and k < oldArr_length:
        oldArr[k] = leftArr[i]
        i += 1
        k += 1
    while j < rightArr_length and k < oldArr_length:
        oldArr[k] = rightArr[j]
        j += 1
        k += 1


def mergeSort(arr, length):
    if length <= 1:
        return
    
    leftArr_length = length // 2
    rightArr_length = length - leftArr_length
    leftArr = []
    rightArr = []

    for i in range(0, leftArr_length):
        leftArr.append(arr[i])
    for j in range(0, rightArr_length):
        rightArr.append(arr[leftArr_length + j])
    
    mergeSort(leftArr, leftArr_length)
    mergeSort(rightArr, rightArr_length)

    merge(arr, length, leftArr, leftArr_length, rightArr, rightArr_length)


if __name__ == "__main__":
    print("------- Initial Arr -------")
    print(g_arr)
    mergeSort(g_arr, len(g_arr))
    print("------- Final Arr -------")
    print(g_arr)

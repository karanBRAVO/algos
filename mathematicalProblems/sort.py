def swap(arr: list, i: int, j: int):
    temp = arr.copy()
    arr[i] = arr[j]
    arr[j] = temp[i]


def partition(arr: list,  start: int, end: int, startIndex: int, endIndex: int):
    pivotValue = arr[startIndex]

    while start < end:
        while arr[start] <= pivotValue:
            if start == endIndex:
                break
            start += 1
        while arr[end] > pivotValue:
            if end == startIndex:
                break
            end -= 1
        if start < end:
            swap(arr, start, end)
    if start >= end:
        swap(arr, startIndex, end)
    return end


def quickSort(arr: list, start: int, end: int):
    if start >= end:
        return arr
    index = partition(arr, start, end, start, end)
    quickSort(arr, start, index - 1)
    quickSort(arr, index + 1, end)
    return arr


nums = [5,4,3,2,1]
print(quickSort(nums, 0, len(nums) - 1))

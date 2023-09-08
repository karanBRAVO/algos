myArr = [10, 200, 100, 20, 39, 89, 65, 34, 55, 234, 43, 1]

def insertionSort(arr):
    i = 1
    while i < len(arr):
        value = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > value:
                arr[j + 1] = arr[j]
                arr[j] = value
            j -= 1
        i += 1

if __name__ == "__main__":
    insertionSort(myArr)
    print(myArr)
myArr = [10, 200, 100, 20, 39, 89, 65, 34, 55, 234, 43, 1]

def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if myArr[i] > myArr[j]:
                swap(arr, i, j)

if __name__ == "__main__":
    selectionSort(myArr)
    print(myArr)

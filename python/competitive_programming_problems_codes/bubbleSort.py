myArr = [10, 200, 100, 20, 39, 89, 65, 34, 55, 234, 43, 1]

def bubbleSort(arr):
    for k in range(0, len(arr) - 1):
        for index in range(0, len(arr) - (k + 1)):
            if arr[index] > arr[index + 1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp

if __name__ == "__main__":
    bubbleSort(myArr)
    print(myArr)
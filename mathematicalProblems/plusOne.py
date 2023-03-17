def plusOneFunc(arr: list) -> list:
    if arr[len(arr) - 1] < 9:
        arr[len(arr) - 1] += 1
    else:
        numStr = ""
        lst = []
        for ele in arr:
            numStr += str(ele)
        num = int(numStr) + 1
        numStr = str(num)
        for i in numStr:
            lst.append(int(i))
        arr = lst
    return arr


arr = [int(x) for x in input().split()]
print(plusOneFunc(arr=arr))

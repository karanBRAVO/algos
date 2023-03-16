def getRow(rowIndex: int) -> list[int]:
    old_arr = [1]
    if rowIndex == 0:
        return old_arr
    else:
        index = 0
        while index < rowIndex:
            ans_arr = []
            ans_arr.append(1)
            for i in range(0, len(old_arr) - 1, 1):
                ans_arr.append(old_arr[i] + old_arr[i + 1])
            ans_arr.append(1)
            old_arr = ans_arr.copy()
            index += 1
        return ans_arr


rowIndex = int(input("Enter the row index: "))
print(getRow(rowIndex=rowIndex))

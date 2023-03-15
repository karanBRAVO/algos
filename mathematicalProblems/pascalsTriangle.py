def generate(numRows: int) -> list[list[int]]:
    ans_arr = [[1]]
    old_arr = [1]

    while len(ans_arr) < numRows:
        if numRows == 1:
            break
        new_arr = []
        new_arr.append(1)
        for i in range(0, len(old_arr) - 1, 1):
            s = old_arr[i] + old_arr[i + 1]
            new_arr.append(s)
        new_arr.append(1)
        ans_arr.append(new_arr)
        old_arr = new_arr.copy()

    return ans_arr


numRows = int(input("Enter the number of rows: "))
print(generate(numRows=numRows))

def minimumTotal(triangle: list[list[int]]) -> int:
    row = 0
    col = 0
    total = triangle[row][col]
    ans = [[row, col]]
    for row in range(1, len(triangle)):
        print("row=", row)
        if triangle[row][col] < triangle[row][col+1]:
            total += triangle[row][col]
        elif triangle[row][col] > triangle[row][col+1]:
            total += triangle[row][col+1]
            col += 1
        elif triangle[row][col] == triangle[row][col+1]:
            ans = checkNextRow_ifSame(triangle, row, col)
            col = ans[0]
            total += ans[1]
            print(col)
        ans.append([row, col])
    print(ans)
    return total


def checkNextRow_ifSame(triangle: list, row: int, col: int):
    print(row, col)
    total = 0
    print(triangle[row+1][col], triangle[row+1][col+1], triangle[row+1][col+2])
    if row < len(triangle) - 1:
        if triangle[row+1][col] < triangle[row+1][col+1] and triangle[row+1][col] < triangle[row+1][col+1+1]:
            print("k")
            total += triangle[row+1][col]
            pass
        elif triangle[row+1][col+1] < triangle[row+1][col+1+1] and triangle[row+1][col+1] < triangle[row+1][col]:
            print("a")
            total += triangle[row+1][col+1]
            col += 1
        elif triangle[row+1][col+1+1] < triangle[row+1][col] and triangle[row+1][col+1+1] < triangle[row+1][col+1]:
            print("r")
            total += triangle[row+1][col+1+1]
            col += 2
        else:
            print("an")
            return checkNextRow_ifSame(triangle, row + 1, col)
    return [col, total]


triangle = [[2], [3, 3], [4,5,4], [6,3,1,5]]
print(minimumTotal(triangle=triangle))

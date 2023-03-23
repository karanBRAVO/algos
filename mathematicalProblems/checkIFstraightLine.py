def checkStraightLine(coordinates: list[list[int]]) -> bool:
    # y = m * x + c
    y2 = coordinates[1][1]    
    y1 = coordinates[0][1]
    x2 = coordinates[1][0]
    x1 = coordinates[0][0]

    try:
        slope = (y2 - y1) / (x2 - x1)
        constant = y1 - (slope * x1)
        for i in range(0, len(coordinates), 1):
            if coordinates[i][1] == slope * coordinates[i][0] + constant:
                continue
            else:
                return False    
        return True
    except ZeroDivisionError:
        x = coordinates[0][0]
        for i in range(0, len(coordinates), 1):
            if coordinates[i][0] == x:
                continue
            else:
                return False
        return True


co_ords = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates=co_ords))

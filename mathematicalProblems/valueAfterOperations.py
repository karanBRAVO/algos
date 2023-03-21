def finalValueAfterOperations(operations: list[str]) -> int:
    x = 0
    for i in range(0, len(operations)):
        if operations[i][0] == "-" or operations[i][len(operations[i]) - 1] == "-":
            x -= 1
        elif operations[i][0] == "+" or operations[i][len(operations[i]) - 1] == "+":
            x += 1
    return x


oprs = ["X++","++X","--X","X--"]
print(finalValueAfterOperations(operations=oprs))

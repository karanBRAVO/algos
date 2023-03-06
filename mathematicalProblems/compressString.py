def compressString(chars):
    arr = []
    doneArr = []
    previousVal = None

    for i in range(len(chars)):
        if previousVal == chars[i]:
            continue

        alreadyDone = False
        if len(doneArr) > 0:
            for k in range(len(doneArr)):
                if chars[i] == doneArr[k]:
                    alreadyDone = True
                    break
        if alreadyDone:
            continue
        doneArr.append(chars[i])

        s = chars[i]
        previousVal = s
        for j in range(len(chars)):
            if chars[j] == chars[i] and j != i:
                s += chars[j]

        arr.append(s[0])
        if len(s) > 1:
            if len(s) >= 10:
                numStr = str(len(s))
                for num in numStr:
                    arr.append(f"{num}")
            else:
                arr.append(f"{len(s)}")

    return arr


print(compressString(["a","a","b","b","c","c","c"]))

def addTo_ArrayForm(num: list[int], k: int) -> list[int]:
    num_str = ""
    for i in range(0, len(num)):
        num_str += str(num[i])
    num = int(num_str)
    ans = num + k
    ans_str = str(ans)
    ans_arr = [0] * len(ans_str)
    for i in range(0, len(ans_str)):
        ans_arr[i] = int(ans_str[i])
    return ans_arr


num = [2,1,5]
k = 806
print(addTo_ArrayForm(num=num, k=k))

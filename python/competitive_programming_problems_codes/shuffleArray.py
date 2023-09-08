def shuffle(nums: list[int], n: int) -> list[int]:
    ans_arr = [0] * len(nums)
    k = 0
    i = 0
    while k < n:
        ans_arr[i] = nums[k]
        ans_arr[i + 1] = nums[k + n]
        i += 2
        k += 1
    return ans_arr


nums = [1, 2]
n = 1
print(shuffle(nums, n))

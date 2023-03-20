def getConcatenation(nums: list[int]) -> list[int]:
    ans = [0] * 2 * len(nums)
    for i in range(0, len(nums), 1):
        ans[i] = nums[i]
        ans[i + len(nums)] = nums[i]
    return ans


nums = [1, 3, 2, 1]
print(getConcatenation(nums=nums))

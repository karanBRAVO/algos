def canBeIncreasing(nums: list[int]) -> bool:
    for i in range(0, len(nums), 1):
        arr = getNewArr(nums, i)
        check = checkStrictlyIncreasing(arr=arr)
        if check:
            return check


def checkStrictlyIncreasing(arr: list) -> bool:
    for i in range(1, len(arr), 1):
        if arr[i] <= arr[i-1]:
            return False
    return True


def getNewArr(arr: list, index: int) -> list:
    ans = []
    for i in range(0, len(arr), 1):
        if i != index:
            ans.append(arr[i])
    return ans


nums = [105, 924, 32, 968]
print(canBeIncreasing(nums=nums))

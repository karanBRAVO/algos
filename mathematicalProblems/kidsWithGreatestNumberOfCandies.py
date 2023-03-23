def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    ans = [False] * len(candies)
    max_value = get_maxIndex_maxValue(candies)
    for i in range(0, len(candies)):
        if candies[i] + extraCandies >= max_value:
            ans[i] = True
    return ans

def get_maxIndex_maxValue(arr: list) -> int:
    max_ele = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_ele:
            max_ele = arr[i]
    return max_ele


candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies=candies, extraCandies=extraCandies))

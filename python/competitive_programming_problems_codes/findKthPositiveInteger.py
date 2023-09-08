class Solution:
    def __init__(self):
        pass

    def checkPresence(self, arr: list, target: int):
        for ele in arr:
            if target == ele:
                return True
        return False

    def findKthPositive(self, arr: list, k: int) -> int:
        index = 0
        value = 1
        while index != k:
            if value < max(arr):
                if not self.checkPresence(arr, value):
                    index += 1
            elif value > max(arr):
                index += 1
            if index == k:
                break
            value += 1
        return value


arr = [1,2,3,4]
k = 2
sol = Solution()
print(f"The missing value at index {k} is {sol.findKthPositive(arr, k)}")

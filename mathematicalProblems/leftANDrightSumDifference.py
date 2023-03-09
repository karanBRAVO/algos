def leftRigthDifference(nums: list) -> list:
    leftSum_arr = []
    rightSum_arr = []
    answer_arr = []

    for i in range(0, len(nums)):
        left_index = i - 1
        leftSum = 0
        while left_index >= 0:
            leftSum += nums[left_index]
            left_index -= 1
        leftSum_arr.append(leftSum)
        
        right_index = i + 1
        rightSum = 0
        while right_index < len(nums):
            rightSum += nums[right_index]
            right_index += 1
        rightSum_arr.append(rightSum)

    for j in range(0, len(nums)):
        answer_arr.append(abs(leftSum_arr[j] - rightSum_arr[j]))

    return answer_arr


nums = [1,2,3,4,5,6,7,8,9,10]
print(leftRigthDifference(nums=nums))
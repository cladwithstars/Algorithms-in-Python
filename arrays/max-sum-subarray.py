#kadane's algorithm

def maxSubArray(nums):
        maxSum = nums[0]
        currentSum = nums[0]
        for i in range(1,len(nums)):
            currentSum = max(nums[i] + currentSum, nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
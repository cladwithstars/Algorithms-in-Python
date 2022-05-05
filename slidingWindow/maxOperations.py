def maxOperations(nums, k):
    '''
    leetcode 1679 - a sliding window problem 
    '''
    nums.sort()
    l, r = 0, len(nums) - 1
    res = 0
    while (l < r):
        if nums[l] + nums[r] == k:
            res += 1
            l += 1
            r -= 1
        elif nums[l] + nums[r] > k:
            r -= 1
        else:
            l += 1
    return res


arr = [1, 2, 3, 4]
k = 5
print(maxOperations(arr, k))

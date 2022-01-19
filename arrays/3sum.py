def threeSum(nums):
    def removeDuplicates(arr):
        sets = []
        output = []
        for val in arr:
            if set(val) not in sets:
                output.append(val)
                sets.append(set(val))
        return output
    
    nums = sorted(nums)
    triplets = []
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            vals = [nums[i], nums[l], nums[r]]
            if sum(vals) == 0:
                triplets.append(vals)
                l += 1
            elif sum(vals) < 0:
                l += 1
            elif sum(vals) > 0:
                r -= 1
    # return removeDuplicates(triplets)
    return removeDuplicates(triplets)

nums = [-1,0,1,2,-1,-4]
#sorted nums is [-4, -1, -1, 0, 1, 2]
print(threeSum(nums)) # expect [[-1,-1,2],[-1,0,1]]
                    
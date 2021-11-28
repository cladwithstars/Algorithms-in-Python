import itertools


def canPartition(nums):
    if sum(nums) % 2 != 0:
        return False
    
    
    target = sum(nums) / 2
    
    if nums[0] == target: return True 
    
    sums = [nums[0]]
    
    for num in nums[1:]:
        for s in sums:
            print(num, s, num+s)
            vals = []
            if num + s == target:
                return True
            vals.append(num + s)
        sums += vals
    return False
        

print(canPartition([1, 1, 1, 1, 4]))
print(canPartition([1, 2, 5]))

# print(canPartition([3, 2, 2, 3]))

# print(canPartition([3, 3, 2, 2]))
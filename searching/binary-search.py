def search(nums, target):
    """
    nums is a sorted array. target is the number we're looking for. Return -1 if not present in nums. 
    """
    l, r = 0, len(nums) - 1
    
    while l <= r:
        pivot = (l + r) // 2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            l = pivot + 1
        elif nums[pivot] > target:
            r = pivot - 1
            
    return -1

target = 2
nums = [1, 2,3, 7, 15, 18, 25, 50]

print(search(nums, target)) #expecting index 1


target = 22
nums = [1,3, 7, 15, 18, 22, 25, 50]

print(search(nums, target)) #expecting index 5 

"""
A function that takes an array of stored integers and a key and 
return the index of the first occurence of that key from teh array
"""

def first_duplicate(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return i
    return -1

nums = [1, 2, 3, 108, 108, 243, 243, 285, 277, 401, 401]
print(first_duplicate(nums))
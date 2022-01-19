def searchRange(nums, target):
    '''
    Given an array of integers nums sorted in non-decreasing order, find the starting and 
    ending position of a given target value.

    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.
    '''
    def modifiedBinarySearch(nums, target, findLeftmost: bool):
        startIndex, endIndex = 0, len(nums) - 1
        foundIndex = -1
        while startIndex <= endIndex:
            mid = (startIndex + endIndex) // 2
            if nums[mid] == target:
                foundIndex = mid
                if findLeftmost:
                    endIndex = mid - 1
                else:
                    startIndex = mid + 1
            elif nums[mid] < target:
                startIndex = mid + 1
            elif nums[mid] > target:
                endIndex = mid - 1
                
        return foundIndex
    
    left = modifiedBinarySearch(nums, target, True)
    right = modifiedBinarySearch(nums, target, False)
    return [left, right]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target)) #expect [3, 4]

#explanation: a two pass binary search is needed with this modified goal
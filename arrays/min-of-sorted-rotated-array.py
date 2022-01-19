def findMin(nums):
    startIdx, endIdx = 0, len(nums) - 1
    if len(nums) == 1:
        return nums[0]
    # if nums[0] < nums[-1]: #case where array is already sorted
    #     return nums[0]
    
    #now we know there *is* a pivot point, i.e. array is not already sorted...
    while startIdx < endIdx:
        midIdx = (endIdx + startIdx) // 2
        print(f'startIdx: {startIdx}, endIdx: {endIdx}, midIdx: {midIdx}')
        if nums[startIdx] < nums[endIdx]: #sorted array
            return nums[startIdx]
        if nums[midIdx] < nums[midIdx - 1]: #found pivot
            return nums[midIdx]
        elif nums[midIdx] > nums[startIdx]: #we know we're in the left sorted portion of the array, so min is in right side
            startIdx = midIdx + 1
        elif nums[midIdx] < nums[startIdx]: #we know were' in the right sorted portion of the array, so min is in left side
            endIdx = midIdx - 1
    return nums[startIdx]

nums = [1, 2]
print(findMin(nums))
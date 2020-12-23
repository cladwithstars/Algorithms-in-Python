def bin_search(target, nums):
    #add base cases here:
    startIndex, endIndex = 0, len(nums) - 1
    position = -1
    while position == -1:
        print(f'start: {startIndex}, end: {endIndex}')
        if startIndex > endIndex:
            return -1 #not found, searched the whole list
        midIndex = (startIndex + endIndex) // 2
        
        if nums[midIndex] == target:
            return midIndex
        elif nums[midIndex] > target:
            endIndex = midIndex - 1
        elif nums[midIndex] < target:
            startIndex = midIndex + 1

    return position 

target = 2
nums = [1, 2,3, 7, 15, 18, 25, 50]

print(bin_search(target, nums))

target = 2
nums = [2, 3, 4, 5, 6, 7]
print(bin_search(target, nums))
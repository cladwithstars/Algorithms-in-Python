def insertionSort(nums):
    for i in range(1, len(nums)):
        currentValue =  nums[i]
        currentPosition = i

        
        while currentPosition > 0 and nums[currentPosition - 1] > currentValue:
            nums[currentPosition] = nums[currentPosition -1]
            print(nums)
            currentPosition -= 1


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        nums[currentPosition] = currentValue
    return nums
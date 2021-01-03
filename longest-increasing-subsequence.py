def lengthOfLIS2(nums):
        """
        Write a helper function that checks the LIS starting at a particular index in nums
        
        The function takes in a list and returns the longest increasing subsequence starting at index 0 of that list 
        
        Then all we have to do is return the max length list of all these helper function results to get our final answer
        """
        def helper(l):
            currMax = 1
            for i in range(len(l)):
                currLen = 1
                for j in range(i + 1, len(l)):
                    print(i, j, currLen, currMax)
                    if l[j] > l[i]:
                        j += 1
                        currLen += 1
                        if currLen > currMax:
                            currMax = currLen
                    else:
                        if currLen > currMax:
                            currMax = currLen
                        j+=1
                        currLen = 0
        
            return currMax

        return helper(nums)


# print(lengthOfLIS2([1, 2, 3, 4]))

# print(lengthOfLIS2([2, 2, 3, 4]))

# print(lengthOfLIS2([4, 2, 3, 4]))

# print(lengthOfLIS([7, 2, 1, 4, 8]))

# print(lengthOfLIS([10,9,2,5,3,4, 7,101,18]))

def LIS(nums):
    """
    Algorithm: loop through nums. At each nums of i:

    find closest largest value next to nums of i. E.g. if nums[i + 1] > nums[i], get nums[i + 1]. Else, check nums[i + 2], etc. 

    Keep track of the length of this sequence. Seq length starts at 1 but once we find a val to the right of nums[i], increment seq count to 2. And so on everytime we find a new value
    larger than the one we just found. Return the maximum longest sequence. 
    """
    currMax = 1

    for i in range(len(nums)):
        maxStartingAt = 1
        j = i + 1
        while j < len(nums) and nums[j] < nums[i]:
            j += 1



    return currMax






# print(LIS([7, 2, 1, 4, 8]))

# print(LIS([10,9,2,5,3,7,101,18]))


def longestLIS(nums):
    """ 
    Algorithm: loop through nums. At each nums of i:

    find closest largest value next to nums of i. E.g. if nums[i + 1] > nums[i], get nums[i + 1]. Else, check nums[i + 2], etc. 

    Keep track of the length of this sequence. Seq length starts at 1 but once we find a val to the right of nums[i], increment seq count to 2. And so on everytime we find a new value
    larger than the one we just found. Return the maximum longest sequence. 
    """
    vals = [1 for _ in nums]
    i, j = 0, 1
    while j < len(nums):
        if nums[j] > nums[i]:
            vals[j] += 1
            j+= 1

print(longestLIS([1, 2, 3]))


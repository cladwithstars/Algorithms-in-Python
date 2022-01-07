import collections
def findLHS(nums):
    """
    Return longest harmonious subsequence.
    A harmonious subsequence is a subsequence such that the difference between the min and max element is precisely 1 
    """
    
    counter = collections.Counter(nums) #creates a dict-like object mapping each int to how many times it occurs in nums
    curMax = 0
    for key in counter:
        if key + 1 in counter:
            curMax = max(curMax, counter[key] + counter[key + 1]) 
            
    return curMax

print(findLHS([1,3,2,2,5,2,3,7]))
print(findLHS([1, 1, 1]))

import collections
def productExceptSelf(nums):
    """
    given array of integers, nums, return a new array arr where arr[i] is equal to the product of all ints in nums except the int at index i 
    """

    counterMap = collections.Counter(nums) #maps each int to how many times it occurs in nums array 
    
    rtn = []
    for num in nums:
        prod = 1
        for key in counterMap.keys():
            prod*= key**(counterMap[key] - 1) if key == num else  key**(counterMap[key])
            
        rtn.append(prod)
    
    return rtn 






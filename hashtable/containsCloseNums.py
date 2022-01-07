def solution(nums, k):
    """
    Given an array of integers nums and an integer k, determine whether there are two 
    distinct indices i and j in the array where nums[i] = nums[j] and the absolute 
    difference between i and j is less than or equal to k
    """
    d = dict()

    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]].append(i)
        else:
            d[nums[i]] = [i]
            
    for key in d:
        indices = d[key]
        if len(indices) > 1:
            for i in range(len(indices) - 1):
                if indices[i + 1] - indices[i] <= k:
                    return True
                    
    return False

nums = [0, 1, 2, 3, 5, 2]
k = 3
print(solution(nums, k)) #expect true

nums = [0, 1, 2, 3, 5, 2]
k=2 
print(solution(nums, k)) # expect false
    
def findClosestElements(nums, k, x):
    '''
    problem 658
    '''
    res = []
    for num in nums:
        diff = abs(num - x)
        res.append((num, diff))
    kClosest = sorted(res, key=lambda val: val[1])[:k]
    kClosestSorted = sorted(kClosest, key=lambda val: val[0])
    return [val[0] for val in kClosestSorted]


nums = [1, 2, 3, 4, 5]
k = 4
x = 3
print(findClosestElements(nums, k, x))

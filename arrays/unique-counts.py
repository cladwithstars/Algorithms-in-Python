    
def uniqueCounts(arr):
    """
    Given an array of integers arr, write a function that returns true iff the number of occurrences of each value in the array is unique.
    """
    counts = [arr.count(num) for num in set(arr)]
    return len(counts) == len(set(counts))

L = [1,2,2,1,1,3]
print(uniqueCounts(L))
print(uniqueCounts([1, 1, 2, 2]))
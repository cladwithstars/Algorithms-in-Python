"""
Array Pair sum 
Given an integer array, output all the unique pairs that sum up to a speicifc value k
"""
def aps(L, k):
    # first get all unique pairs
    # then check if that pair equals k
    pairs = set()
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if L[i] + L[j] == k:
                pairs.add((L[i], L[j]))

    return pairs if len(pairs) > 0 else {}

print(aps([1, 3, 2, 2], 4))
print(aps([1, 3, 2, 7], 10))
print(aps([1, 3, 2, 2], 5))
print(aps([1, 4], 3))
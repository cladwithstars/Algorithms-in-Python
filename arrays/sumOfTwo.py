def solution(a, b, v):
    """
    You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of 
    numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. 
    Return true if such a pair exists, otherwise return false
    """
    s = set()
    for i in range(len(b)):
        s.add(v - b[i])
    for i in range(len(a)):
        if a[i] in s:
            return True
    return False

a = [1, 2, 3]
b = [10, 20, 30, 40]
v = 42
print(solution(a, b, v)) #expect true
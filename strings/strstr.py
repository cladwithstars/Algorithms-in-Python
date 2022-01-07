def solution(s, x):
    '''
    Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of 
    the string x in s. The function should return an integer 
    indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.
    '''
    if x not in s:
        return -1
    for i in range(0, len(s) - len(x) + 1):
        if s[i:i + len(x)] == x:
            return i

print(solution('hello', 'll')) #expect 2
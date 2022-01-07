def solution(n):
    """
    You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. 
    Calculate how many distinct ways you can climb to the top of the staircase.

    Problem is equivalent to computing nth element in the Fibonnaci sequence
    """
    if n == 1 or n == 2:
        return n
    v1, v2 = 1, 1
    for i in range(2, n):
        v1, v2 = v2, v1 + v2
    return v1 + v2

print(solution(5)) # expect 8
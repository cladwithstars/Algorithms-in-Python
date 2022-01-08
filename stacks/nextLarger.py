def solution(a):
    '''
    Given an array a composed of distinct elements, find the next larger element for each element 
    of the array, i.e. the first element to the right that is greater than this element, in the
     order in which they appear in the array, and return the results as a new array of the same 
     length. If an element does not have a larger element to its right, put -1 in the appropriate 
     cell of the result array.
    '''
    stack = []
    output = [-1 for _ in range(len(a))]
    for i in range(len(a)):
        while stack and a[stack[-1]] < a[i]:
            output[stack[-1]] = a[i]
            stack.pop()
        stack.append(i)
    return output

nums = [6, 7, 3, 8]
print(solution(nums)) #expect [7, 8, 8, -1]
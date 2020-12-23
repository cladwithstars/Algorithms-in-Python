
#using set inersection (built in operation):
# def intersect_sorted_array(A, B):
#     A = set(A)
#     B = set(B)
#     return list(A.intersection(B))

def intersect_sorted_array(A, B):
    """
    CALCULATE SET OF ELEMENTS COMMON TO BOTH ARRAYS

    Without using set operations

    A, B are two sorted lists
    """
    intersection = set()
    i, j = 0, 0
    while i < len(A) and j < len(B):
        print(i, j)
        if A[i] == B[j]:
            intersection.add(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i+= 1
        elif B[i] < A[i]:
            j+= 1
    return intersection

    
A = [1, 2, 3, 4, 4]
B = [2, 4, 4, 5, 6]
print(intersect_sorted_array(A, B))
print(intersect_sorted_array(A, A))

A = [1, 2, 3, 4, 4]
B = [6, 7, 7]
print(intersect_sorted_array(A, B))
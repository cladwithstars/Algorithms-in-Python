def quickSort(L):
    
    if len(L) < 2:
        return L
    
    pivot = L[0]
    less = [num for num in L[1:] if num <= pivot]
    greater = [num for num in L[1:] if num > pivot]
    
    return quickSort(less) + [pivot] + quickSort(greater)
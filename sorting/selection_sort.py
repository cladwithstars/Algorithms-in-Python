def selectionSort(L):
    if len(L) < 2:
        return L
    
    minIndex = L.index(min(L))
    L[0], L[minIndex] = L[minIndex], L[0]
    return [L[0]] + selectionSort(L[1:])
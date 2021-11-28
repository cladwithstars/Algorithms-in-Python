def bubbleSort(L):
    n = len(L)
    
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if L[j + 1] < L[j]:
                L[j], L[j + 1] = L[j + 1], L[j]
                print(L)
                
    return L
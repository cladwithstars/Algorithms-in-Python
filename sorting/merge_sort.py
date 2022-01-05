def mergeSort(L):
    if len(L) <= 1:
        return L
    
    pivot = len(L)//2
    print('L: ', L)
    
    left = mergeSort(L[:pivot])
    right = mergeSort(L[pivot:])
    
    
    return merge(left, right)
    

def merge(l1, l2):
    '''helper for mergeSort'''
    print('merging: ', (l1, l2))
    newList = []
    
    while l1 and l2:
        if l1[0] < l2[0]:
            newList.append(l1[0])
            l1.remove(l1[0])
            
        else:
            newList.append(l2[0])
            l2.remove(l2[0])
     
    newList += l2 if not l1 else l1

    print('from merge, returning: ', newList)
    return newList 

nums = [4, 2, 88, 6, 55, 34, 1, 7, 15]
print(mergeSort(nums))
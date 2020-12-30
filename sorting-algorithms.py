def mergeSort(L):
    if len(L) <= 1:
        return L
    
    pivot = len(L)//2
    
    left = mergeSort(L[:pivot])
    right = mergeSort(L[pivot:])
    
    return merge(left, right)
    

def merge(l1, l2):
    '''helper for mergeSort'''
    newList = []
    
    while l1 and l2:
        if l1[0] < l2[0]:
            newList.append(l1[0])
            l1.remove(l1[0])
            
        else:
            newList.append(l2[0])
            l2.remove(l2[0])
            
    newList += l2 if not l1 else l1
            
            
    return newList 

def bubbleSort(L):
    n = len(L)
    
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if L[j + 1] < L[j]:
                L[j], L[j + 1] = L[j + 1], L[j]
                print(L)
                
    return L

def quickSort(L):
    
    if len(L) < 2:
        return L
    
    pivot = L[0]
    less = [num for num in L[1:] if num <= pivot]
    greater = [num for num in L[1:] if num > pivot]
    
    return quickSort(less) + [pivot] + quickSort(greater)


def selectionSort(L):
    if len(L) < 2:
        return L
    
    minIndex = L.index(min(L))
    L[0], L[minIndex] = L[minIndex], L[0]
    return [L[0]] + selectionSort(L[1:])
    

def insertionSort(nums):
    for i in range(1, len(nums)):
        currentValue =  nums[i]
        currentPosition = i

        
        while currentPosition > 0 and nums[currentPosition - 1] > currentValue:
            nums[currentPosition] = nums[currentPosition -1]
            print(nums)
            currentPosition -= 1


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        nums[currentPosition] = currentValue
    return nums


print(insertionSort([2, 5, 1, 3, 99, 1000, 56]))
# print(quickSort([2, 5, 1, 3, 99, 1000, 56]))
# print(bubbleSort([2, 5, 1, 3, 99, 1000, 56]))
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        l = []
        while self:
            l.append(self.val)
            self = self.next
        l.append(None)
        return str(l)

def mergeLists(l1, l2):
    head = mergedList = ListNode(0)
        
    while l1 and l2:
        if l1.val >= l2.val:
            mergedList.next = l2
            l2 = l2.next
            mergedList = mergedList.next
            
        elif l2.val > l1.val:
            mergedList.next = l1
            l1 = l1.next
            mergedList = mergedList.next
            
    if l2:
        #append rest of l2 to merged list
        mergedList.next = l2
    elif l1:
        #append rest of l1 to merged list
        mergedList.next = l1
    
    return head.next

a = ListNode(1)
b = ListNode(2)
b.next = None
a.next = b
l1 = a 
l2=a

print('mergedList : ', mergeLists(l1, l2))


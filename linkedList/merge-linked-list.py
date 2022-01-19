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

def mergeLists(list1, list2):
    head = mergedList = ListNode(0)
            
    while list1 and list2:
        if list1.val < list2.val:
            mergedList.next = ListNode(list1.val)
            list1 = list1.next
            mergedList = mergedList.next
        else:
            mergedList.next = ListNode(list2.val)
            list2 = list2.next
            mergedList = mergedList.next
            
    mergedList.next = list1 if list1 else list2
    
    return head.next

a = ListNode(1)
b = ListNode(2)
b.next = None
a.next = b
l1 = a 
l2=a

print('mergedList : ', mergeLists(l1, l2))


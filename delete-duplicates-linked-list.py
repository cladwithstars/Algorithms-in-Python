# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    """
    delete duplicate values from linked list.

    E.g. if 1 -> 1 -> 2  is given, return 1 -> 2
    """
    curr = head
    
    while curr:
        while curr.next is not None and curr.next.val == curr.val:
            next_one = curr.next.next
            curr.next = next_one
            
            
            if not curr.next:
                return head
        curr = curr.next
            # curr = curr.next
    
        
    return head
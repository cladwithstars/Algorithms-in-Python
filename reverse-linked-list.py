
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(head):
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        vals.append(None)
        return (str(vals))
        

def reverseList(head):
    """
    1 -> 2 -> NULL
    should become: 2-> 1 -> NULL


    keep track of prev

    start at the head, go through each node one by one
    take 1 
    save this node 
    then 
    
    need to set head.next = NULL at the end
    """
    curr = head
    prev = None

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev


L3 = ListNode(3)
L2 = ListNode(2, L3)
L = ListNode(1, L2)
print('result is', reverseList(L))
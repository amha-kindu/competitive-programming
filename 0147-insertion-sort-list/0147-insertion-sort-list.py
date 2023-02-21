# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        current = head
        prev = dummy
        next_ = None
        while current:
            next_ = current.next
            while prev.next and prev.next.val < current.val:
                prev = prev.next
                
            current.next = prev.next
            prev.next = current
            prev = dummy
            current = next_
        return dummy.next
        
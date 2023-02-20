# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        intersection = None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                intersection = slow
                break
        
        if not intersection:
            return
        
        ptr, entrance = head, intersection
        while ptr != entrance:
            entrance = entrance.next
            ptr = ptr.next
        return entrance
            
        
        
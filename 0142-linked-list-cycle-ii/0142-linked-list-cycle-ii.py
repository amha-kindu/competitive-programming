# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        inter = None
        slow = head
        fast = head.next if head else None
        while fast and fast.next:
            if hash(fast) == hash(slow):
                inter = slow
                break
            slow = slow.next
            fast = fast.next.next
        
        if not inter:
            return
        
        ptr, entrance = head, inter.next
        while hash(ptr) != hash(entrance):
            entrance = entrance.next
            ptr = ptr.next
        return entrance
            
        
        
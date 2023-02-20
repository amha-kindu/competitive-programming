# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        
        current = prev.next
        # Reversing
        for i in range(right - left):
            forward = current.next
            current.next = forward.next
            
            forward.next = prev.next
            prev.next = forward
        return dummy. next;
        
       
            
        
        
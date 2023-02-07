# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode()
        after_head = ListNode()
        
        before_ptr = before_head
        after_ptr = after_head
        
        while head:
            if head.val < x:
                before_ptr.next = ListNode(head.val)
                before_ptr = before_ptr.next
            else:
                after_ptr.next = ListNode(head.val)
                after_ptr = after_ptr.next
                    
            head = head.next
            
        before_ptr.next = after_head.next
        return before_head.next
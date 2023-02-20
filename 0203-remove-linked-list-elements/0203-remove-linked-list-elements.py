# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int, prev=None) -> Optional[ListNode]:
        if not head:
            return
        
        while not prev and head and head.val == val:
            head = head.next
            
        if not head:
            return

        if head.val == val and prev:
            prev.next = head.next
            head.next = None
            self.removeElements(prev.next, val, prev)
        else:
            self.removeElements(head.next, val, head)
        return head
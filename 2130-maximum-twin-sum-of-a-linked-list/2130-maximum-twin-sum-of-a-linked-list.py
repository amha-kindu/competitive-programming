# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head, prev=None):
        if not head:
            return prev
        temp = head.next
        head.next = prev
        return self.reverseList(temp, head)
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow  = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        right_half = self.reverseList(slow.next)
        slow.next = None
        
        max_sum = -float('inf')
        ptr = right_half
        while ptr and head:
            max_sum= max(max_sum, head.val+ptr.val)
            ptr = ptr.next
            head = head.next
        return max_sum
        
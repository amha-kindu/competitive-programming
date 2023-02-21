# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr, l2_ptr = l1, l2
        carry = 0
        sum_head = ListNode(0)
        sum_ptr = sum_head
        while l1_ptr or l2_ptr or carry:
            sum_ = carry
            if l1_ptr:
                sum_ += l1_ptr.val
                l1_ptr = l1_ptr.next
            if l2_ptr:
                sum_ += l2_ptr.val
                l2_ptr = l2_ptr.next
                
            digit = ListNode(sum_ % 10)
            sum_ptr.next = digit
            sum_ptr = sum_ptr.next
            carry = sum_ // 10
        return sum_head.next
            
            
            
        
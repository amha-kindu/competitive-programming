# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, left, right):
        if not left and right:  return right
        if not right and left:  return left

        dummy = ListNode(0)
        answer = dummy
        while left or right:
            left_val = left.val if left else float('inf')
            right_val = right.val if right else float('inf')
            if left_val < right_val:
                dummy.next = ListNode(left_val)
                left = left.next
            else:
                dummy.next = ListNode(right_val)
                right = right.next
            dummy = dummy.next

        return answer.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
            
        if not head.next:
            return head
        
        # Find the middle nod
        mid = head
        fast = head.next
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        temp = mid.next
        mid.next = None
        
        # Divide and Conquer
        left = self.sortList(head)
        right = self.sortList(temp)

        return self.mergeList(left, right)


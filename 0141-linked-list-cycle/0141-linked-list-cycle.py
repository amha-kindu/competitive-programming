# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None
        while fast and fast.next:
            if hash(fast) == hash(slow):
                return True
            slow = slow.next
            fast = fast.next.next
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        ptr = head
        while ptr:
            if ptr in visited:
                return True
            else:
                visited.add(ptr)
            ptr = ptr.next
        return False
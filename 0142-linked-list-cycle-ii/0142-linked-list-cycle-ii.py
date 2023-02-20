# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = 0
        visited = set()
        ptr = head
        while ptr:
            if ptr in visited:
                return ptr
            else:
                visited.add(ptr)
            pos += 1
            ptr = ptr.next
            
        
        
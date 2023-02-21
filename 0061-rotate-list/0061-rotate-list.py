# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotate(self, head):
        ptr = head
        while ptr.next and ptr.next.next:
            ptr = ptr.next
        
        last = ptr.next
        ptr.next = None
        last.next = head
        return last
    
    def length(self, head):
        ptr = head
        cnt = 0
        while ptr:
            cnt += 1
            ptr = ptr.next
        return cnt
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.length(head)
        if n==0:
            return
        for _ in range(k%n):
            if head and head.next:
                head = self.rotate(head)
        
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int)->Optional[ListNode]:
        
        left=head
        right=head
        i=0
        while i<=n and right:
            right=right.next
            i+=1
        
        while right:
            left=left.next
            right=right.next
            i+=1
        
        if i==n:
            head=head.next
        
        if left and left.next:
            left.next=left.next.next
        return head
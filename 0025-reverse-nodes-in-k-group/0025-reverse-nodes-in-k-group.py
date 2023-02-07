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
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead, winPrev, winHead = None, None, head
        count = 1
        while head:
            temp = head.next
            if count == k:
                head.next = None
                reversed_part = self.reverseList(winHead)
                if not newHead:
                    newHead = reversed_part
                if winPrev:
                    winPrev.next = reversed_part
                winPrev = winHead
                winHead = temp
                count = 1
            else:
                count += 1
            
            head = temp
        winPrev.next = winHead
        return newHead
                
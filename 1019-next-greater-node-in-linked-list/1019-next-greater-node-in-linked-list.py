# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        ptr = head
        mono_stack = []
        next_ = {}
        i = 0
        while ptr:
            while len(mono_stack) > 0 and ptr.val > mono_stack[-1][1]:
                next_[mono_stack.pop()] = ptr.val
            
            mono_stack.append( (i,ptr.val) )
            
            i+=1
            ptr = ptr.next
            
        while len(mono_stack)>0:
            next_[mono_stack.pop()] = 0
            
        answer = []
        ptr = head
        i = 0
        while ptr:
            answer.append(next_[(i, ptr.val)])
            i+=1
            ptr = ptr.next
        return answer
                
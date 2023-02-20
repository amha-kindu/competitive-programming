# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = None
        odd_ptr = None

        even_head = None
        even_ptr = None
        i = 1
        ptr = head
        while ptr:
            temp = ptr.next
            ptr.next = None
            if i % 2 != 0:
                if odd_ptr:
                    odd_ptr.next = ptr
                    odd_ptr = odd_ptr.next
                else:
                    odd_ptr = ptr
                    odd_head = odd_ptr
            else:
                if even_ptr:
                    even_ptr.next = ptr
                    even_ptr = even_ptr.next
                else:
                    even_ptr = ptr
                    even_head = even_ptr

            ptr = temp
            i+=1
        if odd_ptr:
            odd_ptr.next = even_head
        return odd_head
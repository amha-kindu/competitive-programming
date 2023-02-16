# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ListNode* reverseList(ListNode* head, ListNode* prev=nullptr){
#         if(head==nullptr) return prev;
#         ListNode* temp = head->next;
#         head->next=prev;
#         return reverseList(temp, head);
#     }

#     bool isPalindrome(ListNode* head) {
#         ListNode* slow = head;
#         ListNode* fast = head->next;
#         if(fast==nullptr)   return true;
        
#         while(fast!=nullptr&&fast->next!=nullptr){
#             slow = slow->next;
#             fast = fast->next->next;
#         }
#         ListNode* otherHalf = reverseList(slow->next);
#         slow->next=nullptr;

#         while(otherHalf!=nullptr&&head!=nullptr){
#             if(otherHalf->val!=head->val)   return false;
#             otherHalf=otherHalf->next;
#             head=head->next;
#         }
#         return true;   
#     }
class Solution:
    def reverseList(self, head, prev=None):
        if not head:
            return prev
        temp = head.next
        head.next = prev
        return self.reverseList(temp, head)
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        if not fast:
            return True
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        other_half = self.reverseList(slow.next)
        slow.next = None
        
        while other_half and head:
            if other_half.val != head.val:
                return False
            other_half = other_half.next
            head = head.next
        return True
        
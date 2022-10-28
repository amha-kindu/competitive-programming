/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head, ListNode* prev=nullptr){
        if(head==nullptr) return prev;
        ListNode* temp = head->next;
        head->next=prev;
        return reverseList(temp, head);
    }

    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        if(fast==nullptr)   return true;
        
        while(fast!=nullptr&&fast->next!=nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* otherHalf = reverseList(slow->next);
        slow->next=nullptr;

        while(otherHalf!=nullptr&&head!=nullptr){
            if(otherHalf->val!=head->val)   return false;
            otherHalf=otherHalf->next;
            head=head->next;
        }
        return true;   
        
    }
};
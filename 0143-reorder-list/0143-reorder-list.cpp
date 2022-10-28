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
        if(head==nullptr)   return prev;
        ListNode* temp = head->next;
        head->next = prev;
        return reverseList(temp, head);
    }
    ListNode* merge(ListNode* left, ListNode* right){
        if(left==nullptr)   return right;
        if(right==nullptr)  return left;
        
        ListNode* nextLeft = left->next;
        left->next = right;
        right->next = merge(nextLeft, right->next);
        return left;
        
    }
    void reorderList(ListNode* head) {
        ListNode* fast=head->next;
        ListNode* slow = head;
        while(fast!=nullptr&&fast->next!=nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* right = slow->next;
        slow->next = nullptr;
        right = reverseList(right);
        merge(head, right);
        
    }
};
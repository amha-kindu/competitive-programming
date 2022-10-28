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
    ListNode* swapPairs(ListNode* head, ListNode* prev=nullptr) {
        if(head==nullptr)   return head;
        if(head->next==nullptr)   return head;
        ListNode* temp = head->next;
        head->next=temp->next;
        temp->next=head;
        if(prev!=nullptr)   prev->next=temp;
        swapPairs(head->next, head);
        return temp;
    }
};
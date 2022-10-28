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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2, int carry=0) {
        if(l1==nullptr && l2==nullptr){
            if(carry!=0)    return new ListNode(carry);
            return l1; 
        }

        int sum = carry;
        ListNode* next_l1;
        ListNode* next_l2;
        if(l1!=nullptr){
            sum+=l1->val; 
            next_l1 = l1->next;
        }
        else {l1 = l2;}
        
        if(l2!=nullptr){
            sum+=l2->val; 
            next_l2 = l2->next;
        }
        l1->val = sum % 10; 
        l1->next = addTwoNumbers(next_l1, next_l2, sum/10);
        return l1;
        
    }
};
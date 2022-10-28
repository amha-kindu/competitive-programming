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
    
    int pairSum(ListNode* head) {
        int sum=INT_MIN;
        ListNode* slow = head;
        ListNode* fast = head->next;
        ListNode* prev;
        while(fast->next!=nullptr){
            prev = fast;
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* half = reverseList(slow->next);
        slow->next=nullptr;
        while(half!=nullptr&&head!=nullptr){
            sum = max(sum, half->val+head->val);
            half=half->next;
            head=head->next;
        }
        return sum;
    }
};
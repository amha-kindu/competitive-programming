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

    ListNode* reverseKGroup(ListNode* head, int k){
        ListNode *newHead=NULL,*winPrev=NULL, *winHead=head;
        int count=1;
        while(head!=nullptr){
            ListNode* temp = head->next;
            if(count==k){
                head->next = nullptr;
                ListNode* reversed = reverseList(winHead);
                if(newHead==nullptr)    newHead=reversed;
                if(winPrev!=nullptr)    winPrev->next=reversed;
                winPrev=winHead;
                winHead=temp;
                count=1;
            }
            else   count++;
            head=temp;
        }
        winPrev->next=winHead; 
        return newHead;
    }
};
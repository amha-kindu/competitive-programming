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
    ListNode* insertionSortList(ListNode* head) {
        int swap_count;
        while(swap_count!=0){
            swap_count = 0;
            ListNode* node = head;
            while(node!=nullptr&&node->next!=nullptr){
                if(node->val > node->next->val) {
                    int temp = node->val;
                    node->val = node->next->val;
                    node->next->val=temp;
                    swap_count++;
                }
                node=node->next;
            }
        }
        return head;
    }
};
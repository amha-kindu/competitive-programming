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
    ListNode* mergeList(ListNode* list1, ListNode* list2){
        if(list1==nullptr)  return list2;
        if(list2==nullptr)  return list1;
        if(list1->val<list2->val){
            list1->next = mergeList(list1->next, list2);
            return list1;
        }else{
            list2->next = mergeList(list1, list2->next);
            return list2;
        }
    }

    ListNode* sortList(ListNode* left) {
        if(left==nullptr)   return left;
        if(left!=nullptr&&left->next==nullptr) return left;

        ListNode *middle=left, *fast=left->next;
        while(fast!=nullptr&&fast->next!=nullptr){
            middle=middle->next;
            fast=fast->next->next;
        }
        ListNode* right = middle->next;
        middle->next=nullptr;

        left = sortList(left);
        right = sortList(right);
        return mergeList(left, right);
    }
};
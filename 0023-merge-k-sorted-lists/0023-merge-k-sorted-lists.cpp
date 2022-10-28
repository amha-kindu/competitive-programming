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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size()==0) return nullptr;
        if(lists.size()==1) return lists[0];
        ListNode* last=lists.back();    lists.pop_back();
        ListNode* last2=lists.back();   lists.pop_back();
        ListNode* temp = mergeList(last, last2);
        lists.push_back(temp);
        return mergeKLists(lists);
    }
};
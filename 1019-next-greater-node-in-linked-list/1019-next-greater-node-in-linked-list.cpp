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
    vector<int> nextLargerNodes(ListNode* head) {
        stack<vector<int>> mono;
        map<int, int> next;
        int i = 0;
        while(head!=nullptr){
            while(!mono.empty()&&head->val>mono.top()[1]){
                next[mono.top()[0]]=head->val;
                mono.pop();
            }
            vector<int> val = {i, head->val};
            mono.push(val);
            i++;
            head=head->next;
        }
        while(!mono.empty()){
            next[mono.top()[0]]=0;
            mono.pop();
        }
        vector<int> nextLarger(i);
        for(auto h: next)   nextLarger[h.first]=h.second;
        return nextLarger;
    }
};
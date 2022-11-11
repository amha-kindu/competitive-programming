class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> mp;
        for(int n: arr) mp[n]++;
        
        priority_queue<int> cnt;
        for(auto it: mp)    cnt.push(it.second);
        
        int i=0, removed=0;
        while(!cnt.empty()>0&&removed<arr.size()/2){
            removed+=cnt.top();
            cnt.pop();   i++;
        }
        return i;
    }
};
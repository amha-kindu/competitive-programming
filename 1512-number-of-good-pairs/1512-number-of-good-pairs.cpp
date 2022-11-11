class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int goodPairs=0;
        for(int i: unordered_set(nums.begin(), nums.end())){
            int n = count(nums.begin(), nums.end(), i);
            goodPairs+=n*(n-1)/2;
        }
        return goodPairs;
    }
};
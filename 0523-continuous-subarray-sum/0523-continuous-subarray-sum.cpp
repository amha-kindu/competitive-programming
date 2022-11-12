class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> hp{{0, 0}};
        int prefix = 0;   
        for (int i = 0; i < nums.size(); i++){
            prefix += nums[i];
            if(hp.find(prefix%k)==hp.end()) hp[prefix%k]=i+1;
            else if(hp[prefix % k] < i)  return true;
        }
        return false;
    }
};
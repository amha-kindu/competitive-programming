class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefixCount({{0,1}});
        int prefix=0, count=0;
        for(int num: nums){
            prefix+=num;
            if(prefixCount.find(prefix-k)!=prefixCount.end())
                count+=prefixCount[prefix-k];
            prefixCount[prefix]++;
        }
        return count;
    }
};
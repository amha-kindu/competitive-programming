class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long l=0, r=-1, total=0, cnt=0;
        while(++r<nums.size()){
            total+=nums[r];
            while(nums[r]*(r-l+1)>total+k)  total-=nums[l++];
            cnt = max(r-l+1, cnt);
        }
        return (int)cnt;
    }
};
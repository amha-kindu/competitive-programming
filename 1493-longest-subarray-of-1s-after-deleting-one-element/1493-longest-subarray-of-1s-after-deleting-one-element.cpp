class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int l=0, r=0, zeros=0, maxLength=0, n=nums.size();
        while(r<n){
            if(nums[r]==0)  zeros++;
            while(zeros>1){
                if(nums[l]==0)  zeros--;
                l++;
            }
            if(r-l>maxLength) maxLength=r-l;
            r++;
        }
        return maxLength;
    }
};
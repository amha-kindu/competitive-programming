class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
    int left=0, right=0, max_length=0, zeroCount=0;
    while(right<nums.size()){
        if(nums[right]==0)  zeroCount++;
        if(zeroCount>k){
            if(nums[left]==0)    zeroCount--;
            left++;
        }
        if(right-left+1>max_length) max_length=right-left+1;
        right++;
    }
    return max_length;
}
};
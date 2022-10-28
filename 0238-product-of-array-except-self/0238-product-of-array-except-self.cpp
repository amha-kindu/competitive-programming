class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefixP(nums.size());
        int n=nums.size();
        prefixP[0]=nums[0];
        for(int i=1;i<n;i++){
            prefixP[i]=prefixP[i-1]*nums[i];
        }
        //return prefixP;
        for(int i=2;i<n;i++){
            nums[n-i]=nums[n-i+1]*nums[n-i];
        }
        //return nums;
        nums[0]=nums[1];
        for(int i=1;i<n-1;i++){
            nums[i]=nums[i+1]*prefixP[i-1];
        }
        nums[n-1]=prefixP[n-2];
        return nums;
    }
};
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int l=0, r=nums.size()-1, count=0;
        while(r>l){
            if(nums[l]+nums[r]>k)   r--;
            else if(nums[l]+nums[r]<k)   l++;
            else{
                count++;
                l++;    r--;
            }
        }
        return count;
    }
};
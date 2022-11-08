class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), end=n%2==0?n/2:1+n/2;
        vector<int> rearranged(n);
        for(int i=0;i<end;i++){
            rearranged[2*i]=nums[i];
            if(i+end<n)
                rearranged[2*i+1]=nums[i+end];
        }
        return rearranged;
    }
};
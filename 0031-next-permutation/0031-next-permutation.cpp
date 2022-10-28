class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        auto p=nums.end()-2;
        if(nums.size()==1)  return;
        while(p>=nums.begin()&&(*(p+1))<=*p)  p--;
        if(p>=nums.begin()){
            auto l=nums.end()-1;
            while (*l <= *p)    l--;
            int temp=*p;
            *p = *l;
            *l = temp;
        }
        reverse(p+1, nums.end());
    }
};
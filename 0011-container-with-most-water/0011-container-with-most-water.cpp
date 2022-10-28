class Solution {
public:
    int maxArea(vector<int>& height) {
        int left=0, right=height.size()-1,max_vol=0;
        while (right>left){
            int new_vol=min(height[right],height[left])*(right-left);
            max_vol=max(max_vol,new_vol);
            
            if(height[left]>height[right]){
                right--;
            }else{
                left++;
            }

        }
        return max_vol;
    }
};
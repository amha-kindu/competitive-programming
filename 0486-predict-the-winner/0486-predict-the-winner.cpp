class Solution {
public:  
    int scoreDiff(vector<int>& nums, int i, int j, int turn){
        if(i>=j)    return turn*nums[i];
        
        int x = nums[i] + turn*scoreDiff(nums, i+1, j, -turn);
        int y = nums[j] + turn*scoreDiff(nums, i, j-1, -turn);
        
        return turn * max(x, y);
    }

    bool PredictTheWinner(vector<int>& nums) {
        return scoreDiff(nums, 0, nums.size()-1, 1) >=0;
    }
};
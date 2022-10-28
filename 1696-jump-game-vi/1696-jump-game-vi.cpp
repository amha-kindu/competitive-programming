class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();

        deque<int> score{0};
        
        for(int i=1;i<n;i++){
            // Remove those out of bound of the atmost k-step requirement
            while(!score.empty() && score.front()<i-k)  score.pop_front();
            
            nums[i] = nums[i]+nums[score.front()];
            
            //Keep the monotonocity of the queue
            while(!score.empty() && nums[i]>=nums[score.back()])    score.pop_back();
            score.push_back(i);
        }
        
        return nums.back();
    }
};
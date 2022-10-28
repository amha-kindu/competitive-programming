class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int left=0, right=0;
        deque<int> min_queue;
        deque<int> max_queue;
        int maxLength=-INT_MAX;
        
        while(right<nums.size()){
            
            while(!min_queue.empty() && nums[right]<nums[min_queue.back()])   min_queue.pop_back();
            min_queue.push_back(right);
            
            while(!max_queue.empty() && nums[right]>nums[max_queue.back()])   max_queue.pop_back();
            max_queue.push_back(right);
            
            while(!min_queue.empty() && (min_queue.front()<left || min_queue.front()>right))   min_queue.pop_front();
            while(!max_queue.empty() && (max_queue.front()<left || max_queue.front()>right))   max_queue.pop_front();
            
            if(nums[max_queue.front()]-nums[min_queue.front()]<=limit){
                int newLength = right-left+1;
                if(newLength>maxLength) maxLength=newLength;
                right++;
            }else{
                left++;
            }
        }
        return maxLength;
    }
};
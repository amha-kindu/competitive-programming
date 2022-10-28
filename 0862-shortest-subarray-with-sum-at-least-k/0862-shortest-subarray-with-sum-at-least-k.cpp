class Solution {
public:
    
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefixSum={0};
        for(int i: nums)    prefixSum.push_back(prefixSum.back()+i);

        int minLength=n+1;
        deque<int> deque;
        
        for(int i=0; i<n+1; i++){
            // Maintain monotonocity when adding to deque
            while (!deque.empty() && prefixSum[deque.back()]>=prefixSum[i]){
                deque.pop_back();
            }
            
            while (!deque.empty() && prefixSum[i] - prefixSum[deque.front()]>=k){
                int newLength = i - deque.front();
                deque.pop_front();
                if(newLength<minLength) minLength=newLength;
            }
            deque.push_back(i);
        }
        
        if(minLength<n+1)   return minLength;
        return -1;   
    }
};
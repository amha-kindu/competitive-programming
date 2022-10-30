
class KthLargest {
    int k;
    priority_queue<int, vector<int>, greater<int>> pq;
public:

    KthLargest(int k, vector<int>& nums){
        this->k = k;
        pq = priority_queue<int, vector<int>, greater<int>>(nums.begin(), nums.end());
        while(pq.size() > k)    pq.pop();
    }
    
    int add(int val){
        pq.push(val);
        if(pq.size()>k) pq.pop();
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */

 // make_heap(nums.begin(), nums.end());
 //        int i=-1;
 //        while(++i<k-1){
 //            pop_heap(nums.begin(), nums.end());
 //            nums.pop_back();
 //        }
 //        return nums.front();
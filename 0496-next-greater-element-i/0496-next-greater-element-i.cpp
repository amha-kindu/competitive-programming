class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> stack;
        map<int, int> nextGreater;
        
        for(int i: nums2){
            nextGreater[i]=-1;
            while(!stack.empty() && i>stack.top()){
                int value = stack.top();
                stack.pop();
                nextGreater[value] = i;
            }
            stack.push(i);
        }
        
        for(int j=0;j<nums1.size();j++) nums1[j]=nextGreater[nums1[j]];
        return nums1;
    }
};
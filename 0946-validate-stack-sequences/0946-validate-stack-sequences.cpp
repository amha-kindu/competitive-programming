class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int n = pushed.size();
        int left=0, right=0;
        
        stack<int> my_stack;
        
        while(right<n){
            
            if(my_stack.empty() || my_stack.top()!=popped[right]){
                my_stack.push(pushed[left]);
                if(left+1>=n){
                    left=0;
                }else{
                    left++;
                }
        
            }else if(my_stack.top()==popped[right]){
                my_stack.pop();
                right++;
            }
        }

        return my_stack.size()==0;
    }
};
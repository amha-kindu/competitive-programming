class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n=temperatures.size();
        stack<int> mono_stack;
        vector<int> answer(n);
        
        for(int t=0;t<n;t++){
            while(!mono_stack.empty() && temperatures[t]>temperatures[mono_stack.top()]){
                answer[mono_stack.top()] = t-mono_stack.top();
                mono_stack.pop();
                
            }
            mono_stack.push(t);
        }
        return answer;
    }
};
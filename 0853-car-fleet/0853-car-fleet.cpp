class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        stack<int> mono_stack;
        map<int, float> arrival_time;
        
        for(int i=0;i<n;i++)    arrival_time[position[i]]=(target-position[i])/(1.0*speed[i]);
        
        sort(position.begin(), position.end());
        
        for(int pos: position){
            while(!mono_stack.empty() && arrival_time[pos]>=arrival_time[mono_stack.top()])
                mono_stack.pop();
            
            mono_stack.push(pos);
        }
        return mono_stack.size();
    }
};
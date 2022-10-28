class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        int ans=0;
        sort(nums.begin(),nums.end());
        int n=nums.size();
        queue<int> dupl;
        set<int> elems;
        
        // Find duplicates
        for(int i=0;i<n;i++){
            if(elems.find(nums[i])!=elems.end()) dupl.push(i);
            else elems.insert(nums[i]);
        }

        set<int>::iterator it=next(elems.begin());
        for(;it!=elems.end();it++){
            int start=*prev(it)+1;
            int end=*it;
            for(int d=start;d<end&&!dupl.empty()&&d>nums[dupl.front()];d++){
                
                ans+=d-nums[dupl.front()];
                nums[dupl.front()]=d;
                dupl.pop();
            }
        }
        int p=1;
        int h=*prev(elems.end());
 
        while(!dupl.empty()){
          ans+=h+p-nums[dupl.front()];
            nums[dupl.front()]=h+p;
            p++;
            dupl.pop();
        }
       
        return ans;
        
    }
};
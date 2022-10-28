class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> rightMost;
        for(int i =1;i<=s.size();i++)
            if(i>rightMost[s[i-1]])   rightMost[s[i-1]]=i;
        vector<int> ans;
        int j=0, max_i=1,  count=0;
        while(++j<=s.size()){
            if(rightMost[s[j-1]]>max_i)  max_i=rightMost[s[j-1]];
            if(j==max_i){
                ans.push_back(count+1);
                count=-1;
            }
            count++;
        }
        return ans;
    }
};
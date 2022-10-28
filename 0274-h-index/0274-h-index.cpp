class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n=citations.size();
        sort(citations.begin(), citations.end());
        
        int ans=0;
        for(int h=n-1;h>=0;h--){
            if(citations[h]<n-h) break;
            ans=n-h;
        }
        return ans;
    }
};
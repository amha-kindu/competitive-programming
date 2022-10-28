class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n = arr.size(), maxLength=0;
        if(n<3) return 0;
        int r=0, base=-1;
        while(r<n){
            int left = r-1>=0?arr[r-1]:INT32_MAX;
            int right = r+1<n?arr[r+1]:INT32_MAX;
            if(arr[r]==left)  base=-1;
            if(right>arr[r]&&left>=arr[r]||right>=arr[r]&&left>arr[r]){
                if(base!=-1){
                    // maxLength = max(maxLength, r-base+1);
                    if(r-base+1>maxLength)  maxLength=r-base+1;
                } 
                base = r;
            }
            r++;
        }
        return maxLength;
    }
};
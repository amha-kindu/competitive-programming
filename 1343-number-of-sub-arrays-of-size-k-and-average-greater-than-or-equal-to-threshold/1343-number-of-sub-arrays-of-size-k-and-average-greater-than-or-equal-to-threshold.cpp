class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        auto l=arr.begin(), r=arr.begin();
        int window=0, count=0;
        while(r!=arr.end()){
            window+=*r;
            if(r-l+1==k){
                if(window/k >= threshold)   count++;
                window-=*(l++);
            }
            r++;
        }
        return count;
    }
};
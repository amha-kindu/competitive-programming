class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();
        unordered_map<int, int> baskets;

        int l=0, r=-1, maxNum=0;
        while(++r<n){
            baskets[fruits[r]]++;
            while(baskets.size()>2){
                baskets[fruits[l]]--;
                if(baskets[fruits[l]]==0) baskets.erase(fruits[l]);
                l++;
            }
            if(r-l+1>maxNum)  maxNum=r-l+1;
        }
        return maxNum;
    }
};
class Solution {
public:
    int maxVowels(string s, int k) {
        unordered_set<char> vowels = {'a','e','i','o','u'};
        int window=0, maxCount=0;
        auto l=s.begin(), r=s.begin();
        while(r!=s.end()){
            if(vowels.find(*r)!=vowels.end())   window++;
            if(r-l+1==k){
                if(window>maxCount)   maxCount=window;
                if(vowels.find(*(l++))!=vowels.end())   window--;
            }
            r++;
        }
        return maxCount;
    }
};
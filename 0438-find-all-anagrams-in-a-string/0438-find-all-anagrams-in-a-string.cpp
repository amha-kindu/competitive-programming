class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char, int> window, count;
        for(char c: p)  count[c]++;
        vector<int> answer;
        int l=0, r=0, n = p.size();
        while(r<s.size()){
            window[s[r]]++;
            if(window==count)   answer.push_back(l);
            if(r-l+1==n){
                window[s[l]]--;
                if(window[s[l]]==0) window.erase(s[l]);
                l++;
            }
            r++;
        }
        return answer;
    }
};
class Solution {
public:
    static char asciitolower(char in) {
        if (in <= 'Z' && in >= 'A') 
            return in - ('Z' - 'z');
        return in;
    }
    static bool  isAlphanumeric(char c){
        return (c<='9' && c>='0' || c<='z'&&c>='a');
    }
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), asciitolower);

        string s_mod;
        for(char c: s)
            if(isAlphanumeric(c))   s_mod+=c;
    
        for(int i=0;i<s_mod.size();i++){
            if(s_mod[i]!=s_mod[s_mod.size()-i-1])   
                return false;
        }
        return true;
    }
};
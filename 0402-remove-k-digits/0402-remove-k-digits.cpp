class Solution {
public:
    string removeKdigits(string num, int k) {
        int h=k;
        if(num.length()==1 && k>0){
            return "0";
        }
        string mono;
        for(char i:num){
            while(mono.length()!=0&&k>0&&(int)i<(int)mono.back()){
                k--;
                mono.pop_back();
            }
            mono.push_back(i);
        }
        while(mono.length()>num.length()-h){
            mono.pop_back();
        }
        if(mono!="0")
            mono.erase(0, mono.find_first_not_of("0"));
        if(mono.length()==0){
            return "0";
        }
        return mono;
    }
};
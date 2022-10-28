class Solution {
public:
    string S(int i){
        if(i==1)    return "0";
        string temp=S(i-1)+"1";
        for(int i=temp.size()-2;i>-1;i--)  temp+=temp[i]=='0'?'1':'0';
        return temp;
    }
    
    char findKthBit(int n, int k) {
        return S(n)[k-1];
    }
};
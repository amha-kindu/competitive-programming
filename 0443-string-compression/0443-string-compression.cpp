class Solution {
public:
    int compress(vector<char>& chars) {
        int l=0, r=0, length=0, count=0;
        int i=0;
        while(r<=chars.size()&&l<chars.size()){
            if(r==chars.size()||chars[l]!=chars[r]){
                string s;
                s.push_back(chars[l]);
                if(count!=1)    s += to_string(count);
                // cout<<s<<endl;
                for(int c=0;c<s.size();c++)  chars[i+c]=s[c];
                i+=s.size();
                length+= s.size();
                l=r;    count=0;
            }else{
                count++;
                r++;
            } 
        }
        return length;
    }
};
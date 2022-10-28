
class Solution {
public:
    int calculate(string s) {
        char prevOp='_';
        string currNum;
        int result=0,last=0;
        s+="-";
        
        for(char c:s){
            if((int)c<42) continue;
            if((int)c>47){
                currNum.push_back(c);
            }else{
   
                if(c=='+'||c=='-'){
                    if(prevOp=='-') result-=stoi(currNum);
                    else if(prevOp=='+') result+=stoi(currNum);
                    else if(prevOp=='*') result+= last*stoi(currNum);
                    else if(prevOp=='/') result+=last/stoi(currNum);
                    else result+=stoi(currNum);
                }else{
                    if(prevOp=='-') last=-stoi(currNum);
                    else if(prevOp=='*') last*=stoi(currNum);
                    else if(prevOp=='/') last/=stoi(currNum);
                    else last=stoi(currNum);
                }
                prevOp=c;
                currNum.clear();
            }
        }
       
        return result;
    }
};



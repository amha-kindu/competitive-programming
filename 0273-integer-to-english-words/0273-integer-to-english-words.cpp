map<string, string> DTW({
    {"1","One "},{"2","Two "},{"3","Three "},
    {"4","Four "},{"5","Five "},{"6","Six "},
    {"7","Seven "},{"8","Eight "},{"9","Nine "},
    {"10","Ten "},{"11","Eleven "},{"12","Twelve "},{"13","Thirteen "},
    {"14","Fourteen "},{"15","Fifteen "},{"16","Sixteen "},{"17","Seventeen "},
    {"18","Eighteen "},{"19","Nineteen "},{"20","Twenty "},
    {"30","Thirty "},{"40","Forty "},{"50","Fifty "},{"60","Sixty "},
    {"70","Seventy "},{"80","Eighty "},{"90","Ninety "}
});

map<int, string> powers({
    {2,"Hundred "},{3,"Thousand "},{6,"Million "},{9,"Billion "}
});


class Solution {
public:
    string intToWord(string& num, int i, int j){
    while(num[i]=='0')    i++;  //Remove trailing zeros
        
    if(i>=j)    
        return DTW[string(1,num[j])];
    if((j-i+1)==2 && num[i]=='1'){
        string g = string(1, num[i]);
        g.push_back(num[j]);   
        return DTW[g];
    }
    if((j-i+1)==2){
        string g = string(1, num[i]);
        g.push_back('0');   
        string result = DTW[g];
        if(num[j]!='0') result+=DTW[string(1, num[j])];
        return result;
    }
    int leading = (j-i+1)%3;
    if(leading == 0)    leading = 3;
    if(j-i+1<4)
        leading = 1;
    int zeros = (j-i+1)-leading;
    string prefix;
    if(zeros == 1)  prefix = DTW[num[i]+"0"];
    else   prefix = powers[zeros];
    string lead = (j-i+1)>=3?intToWord(num, i, i+leading-1):"";
    return lead+prefix+intToWord(num, i+leading, j);
}
    
    string numberToWords(int num) {
        if(num==0)  return "Zero";
        string value = to_string(num);
        value = intToWord(value, 0, value.size()-1);   
        value.pop_back();
        return value;
    }
};
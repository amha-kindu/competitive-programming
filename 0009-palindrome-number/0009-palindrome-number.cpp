class Solution {
public:
    bool isPalindrome(int x) {
        if(x<=0) return x==0;
        long long reverse_num=0;
        int num = x, MAX=log(x)/log(10);
        for(int i = 0;i<=MAX;i++){
            reverse_num += (num % 10)*pow(10, MAX-i);
            num /= 10;
        }
        return reverse_num == x;
    }
};
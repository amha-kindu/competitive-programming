#define MOD 1000000007

class Solution {
public:
    long long modPow(long long base, long long exp){
        if(exp==0) return 1;
        long long tmp=modPow(base, exp/2);
        if(exp%2==0){
            return (tmp*tmp)%MOD;
        }else{
            tmp=(tmp*tmp)%MOD;
            base%=MOD;
            return (tmp*base)%MOD;
        }
    }
    
    int minNonZeroProduct(int p) {
        long long nums=pow(2,p);
        nums--;
        long long ans=modPow(nums-1,nums/2);
        return ans*(nums%MOD)%MOD;
    }
};
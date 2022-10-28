#define MOD 1000000007

class Solution {
public:
    int twoSumCount(vector<int>& nums, int target, vector<int>::iterator start){
        int cnt=0;
        auto l = start, r=nums.end()-1;
        while(r>l){
            int sum = *l + *r;
            if(sum>target)  r--;
            else if(sum<target) l++;
            else{
                if(*l==*r){
                    int n=r-l+1;
                    cnt+=(n/2.0)*(n-1);
                    break;
                }
                int temp_l=*l, temp_r=*r;
                int l_cnt=0, r_cnt=0;
                while(*l==temp_l){
                    l_cnt++;    l++;
                }
                while(*r==temp_r){
                    r_cnt++;    r--;
                }
                cnt+=l_cnt*r_cnt;
            }
        }
        return cnt;
    }

    int threeSumMulti(vector<int>& nums, int target){
        sort(nums.begin(), nums.end());
        long long cnt=0;
        for(auto it=nums.begin();it!=nums.end();it++)
            cnt+=twoSumCount(nums, target - (*it), it+1);
        return cnt%MOD;
    }


};
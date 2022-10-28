int numberOfSubarrays(int* nums, int numsSize, int k){
    int l=0, r=0, odds=0, cnt=0,total=0;
    while(r<numsSize){
        if(nums[r]%2!=0){
            odds++;
            if(odds>=k){
                cnt=1;
                while(nums[l++]%2==0) cnt++;
                total+=cnt;
            }
        }else if(odds>=k) total+=cnt;

        r++;
    }
    return total;
}
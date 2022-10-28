

int minSubArrayLen(int target, int* nums, int numsSize){
    int l=0,r=0,sum=0,len=INT_MAX;
    while(r<numsSize){
        sum+=nums[r];
        while(sum>=target){
            if(r-l+1<len) len=r-l+1;
            sum-=nums[l++];
        }
        r++;
    }
    if(len==INT_MAX) len=0;
    return len;
}
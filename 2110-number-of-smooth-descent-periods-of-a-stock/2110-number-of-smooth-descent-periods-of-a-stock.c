

long long getDescentPeriods(int* prices, int pricesSize){
    long long l=0,r=1,cnt=0;
    while(l<pricesSize){
        if(r>=pricesSize||prices[r-1]!=prices[r]+1){
            cnt+=(r-l)*(r-l+1)/2.0L;
            l=r;
        }
        r++;
    }
    return cnt;
}
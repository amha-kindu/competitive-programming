

int chalkReplacer(int* chalk, int chalkSize, int k){
    long long sum=0;
    for(int i=0;i<chalkSize;i++) sum+=chalk[i];

    int i=0, cnt=(k/sum)*sum;
    while(cnt<=k){
        cnt+=chalk[i++];
        if(i>=chalkSize) i=0;
    }
    if(i-1>=0) return i-1;
    else return chalkSize-1;

}
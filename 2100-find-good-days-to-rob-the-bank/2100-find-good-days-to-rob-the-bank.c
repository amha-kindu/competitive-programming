

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodDaysToRobBank(int* security, int securitySize, int time, int* returnSize){
    int nonInc[securitySize];
    int cnt=0;
    nonInc[0]=0;
    for(int i=1;i<securitySize;i++){
        if(security[i-1]>=security[i]) cnt++;
        else cnt=0;
        nonInc[i]=cnt;
    }
    cnt=0;
    int nonDec[securitySize];
    nonDec[securitySize-1]=0;
    for(int i=securitySize-2;i>-1;i--){
        if(security[i+1]>=security[i]) cnt++;
    else cnt=0;
    nonDec[i]=cnt;
    }
    int* ans=malloc(securitySize*sizeof(int));
    *returnSize=0;
    for(int i=0;i<securitySize;i++){
        if(nonInc[i]>=time&&nonDec[i]>=time){
            ans[*returnSize]=i;
            (*returnSize)++;
        }
    }
    return ans;
}
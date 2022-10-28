

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize){
    for(int i=1;i<arrSize;i++){
        arr[i]=arr[i]^arr[i-1];
    }
    int* ans=malloc(queriesSize*sizeof(int));
    
    for(int j=0;j<queriesSize;j++){
        int f=queries[j][0]-1;
        if(f<0) ans[j]=arr[queries[j][1]];
        else ans[j]=arr[f]^arr[queries[j][1]];
    }
    *returnSize=queriesSize;
    return ans;
}
long long max(long long x, long long y){
    if(x>y) return x;
    else return y;
}
long long mostPoints(int** questions, int questionsSize, int* questionsColSize){
    long long dp[200001]={};
    for(int i=questionsSize-1;i>=0;i--){
            dp[i]=max(dp[i+1+questions[i][1]]+questions[i][0], dp[i+1]);
    }
    return dp[0];
}
   
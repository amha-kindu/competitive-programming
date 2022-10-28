

int minimumBuckets(char * street){
    int cnt=0, n=strlen(street);

    for(int i=0;i<n;i++){
        
        if(street[i]!='H') continue;
        if(i+1<n&&street[i+1]=='.'){
            if(i==0||street[i-1]!='B'){
            street[i+1]='B';
            cnt++;
          }
        }else if(i>0&&street[i-1]=='.'){
            street[i-1]='B';
            cnt++;
        }
        else if(i==0&&i==n-1||i==0&&street[i+1]=='H'||i==n-1&&street[i-1]=='H'||street[i-1]=='H'&&street[i+1]=='H') return -1;
        
    }
    return cnt;
}
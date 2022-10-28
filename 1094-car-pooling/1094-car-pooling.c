

bool carPooling(int** trips, int tripsSize, int* tripsColSize, int capacity){
    int maxD=0;
    for(int i=0;i<tripsSize;i++) if(trips[i][2]>maxD) maxD=trips[i][2];
    
    int* pass=calloc(maxD+1,sizeof(int));
    for(int i=0;i<tripsSize;i++){
        pass[trips[i][1]]+=trips[i][0];
        pass[trips[i][2]]-=trips[i][0];
    }
    for(int p=0;p<maxD;p++){
        if(p-1>=0) pass[p]+=pass[p-1];
        if(pass[p]>capacity) return false;
    }
    return true;
        
}
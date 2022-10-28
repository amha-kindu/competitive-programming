class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
         vector<int> passCount(n+1,0);
        for(vector<int> v:bookings){
            passCount[v[0]-1]+=v[2];
            passCount[v[1]]-=v[2];
        }
        for(int i=1;i<n;i++){
            passCount[i]+=passCount[i-1];
        }
        passCount.pop_back();
        return passCount;
}
};
       
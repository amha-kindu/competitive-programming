class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        
        int boatCount = 0;
        int l=0, r=people.size()-1;
        while(r>=l){
            if(people[r]+people[l]<=limit) l++;
            r--;
            boatCount++;
        }
        return boatCount;
    }
};
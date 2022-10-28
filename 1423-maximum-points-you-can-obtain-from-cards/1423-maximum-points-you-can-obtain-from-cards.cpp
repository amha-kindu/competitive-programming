class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int sum = accumulate(cardPoints.begin(), cardPoints.end(),0);
        if(k==n)    return sum;
        auto l=cardPoints.begin(), r=cardPoints.begin();
        int window=0, maxScore=0;
        while(r!=cardPoints.end()){
            window+=*r;
            if(r-l+1==n-k){
                if(sum-window>maxScore)     maxScore=sum-window;
                window-=*(l++);
            }
            r++;
        }
        return maxScore;
    }
};
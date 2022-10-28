class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());
        int l=0, r=tokens.size()-1, score=0, maxScore=0;
        while(r>=l){
            if(power>=tokens[l]){
                power-=tokens[l];
                score++;
                if(score>maxScore)  maxScore=score;
                l++;
            }else if(score>=1){
                power+=tokens[r];
                score--;
                r--;
            }
            else break;
        }
        return maxScore;
    }
};
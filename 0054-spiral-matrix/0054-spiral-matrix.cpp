

enum Turn{
    LEFT=0,RIGHT,UP,DOWN,DN
};
class Solution {
public:

    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int rb=matrix[0].size(), lb=-1,ub=0,bb=matrix.size();
        Turn next= RIGHT;
        if(rb==1) next=DOWN;
        int i=0, j=0,n=rb*bb;
        vector<int> ans;
   
        while(ans.size()<n){
            ans.push_back(matrix[i][j]);
            if(next==RIGHT){
                j++;
                if(j+1>=rb){
                    rb--;
                    next=DOWN;
                }
            }
            else if(next==DOWN){
                i++;
                if(i+1>=bb){
                    bb--;
                    next=LEFT;
                }
            }    
            else if(next==LEFT){
                j--;
                if(j-1<=lb){
                    lb++;
                    next=UP;
                }
            }
            else if(next==UP){
                i--;
                if(i-1<=ub){
                    next=RIGHT;
                    ub++;
                }

            }
        }
        return ans;
    }
};
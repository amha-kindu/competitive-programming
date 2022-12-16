class Solution {
public:
    int hourGlassSum(vector<vector<int>>& grid, int i, int j){
        return grid[i][j]+grid[i][j+1]+grid[i][j+2]+ grid[i+1][j+1] +grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2];
    }
    int maxSum(vector<vector<int>>& grid) {
        int maxSum=INT_MIN, t=0;
        while(t<grid.size()-2){
            int r=0;
            while(r<grid[0].size()-2)
                maxSum = max(maxSum, hourGlassSum(grid, t, r++));
            t++;
        }
        return maxSum;
    }
};
class NumMatrix {
public:
    vector<vector<int>> matrix;
    int rows;
    int columns;
    NumMatrix(vector<vector<int>>& matrix) {
        for(int i=0;i<matrix.size();i++){
            for(int j=1;j<matrix[0].size();j++)
                matrix[i][j]=matrix[i][j-1]+matrix[i][j];
        }
        this->matrix=matrix;
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for(int i = row1;i<=row2;i++){
            int left=0;
            if(col1-1>=0)
                left = matrix[i][col1-1];
            sum+=matrix[i][col2]-left;
        }
        return sum;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
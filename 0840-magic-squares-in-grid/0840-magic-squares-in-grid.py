class Solution:
    def isMagicSquare(self, square, r, c):
        row_sum = [0 for _ in range(3)]
        col_sum = [0 for _ in range(3)]
        diag_sum = [0 for _ in range(2)]
        
        unique_vals = set()
        
        for i in range(r, r+3):
            for j in range(c, c+3):
                unique_vals.add(square[i][j])
                row_sum[i-r] += square[i][j]
                col_sum[j-c] += square[i][j]
                
                if abs(i-r-j+c) == 0:
                    diag_sum[0] += square[i][j]
                if i+j == r+c+2:
                    diag_sum[1] += square[i][j]

        total = set(row_sum+col_sum+diag_sum)
        return len(unique_vals)==9 and max(unique_vals)==9 and len(total)==1
                
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magic_squares = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.isMagicSquare(grid, i, j):
                    magic_squares+=1
        return magic_squares
import numpy as np

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        grid = np.array(grid)
        
        onesRow = grid.sum(axis=1)
        onesCol = grid.sum(axis=0)
        zerosRow = grid.shape[1] - grid.sum(axis=1)
        zerosCol = grid.shape[0] - grid.sum(axis=0)
        
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                diff[i][j] = onesRow[i]+onesCol[j]-zerosRow[i]-zerosCol[j]
            
        return diff
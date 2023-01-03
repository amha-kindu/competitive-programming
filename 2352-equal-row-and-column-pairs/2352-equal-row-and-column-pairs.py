class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        equal_count = 0
            
        for col in range(n):
            grid_col = []
            for row in range(n):
                grid_col.append( grid[row][col] )
                
            for some_row in range(n):
                if grid_col == grid[some_row]:
                    equal_count += 1
     
        return equal_count
            
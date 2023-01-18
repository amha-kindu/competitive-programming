class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        get_max = lambda i, j: max(max(grid[i][j:j+3]), max(max(grid[i+1][j:j+3]), max(grid[i+2][j:j+3])))
        
        answer = []
        
        for r in range(len(grid)-2):
            ans_row = []
            for c in range(len(grid[0])-2):
                ans_row.append(get_max(r, c))
            answer.append(ans_row)
                
        return answer
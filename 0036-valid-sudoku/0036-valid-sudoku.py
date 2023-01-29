class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_nums = [ [] for _ in range(len(board)) ]
        col_nums = [ [] for _ in range(len(board[0])) ]
        subgrid = [[] for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    continue
                    
                row_nums[i].append(board[i][j])
                col_nums[j].append(board[i][j])
                
                subgrid[ (i//3)*3 + (j//3) ].append(board[i][j])
            
        for nums in row_nums+col_nums+subgrid:
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i]==nums[i+1]:
                    return False
        return True

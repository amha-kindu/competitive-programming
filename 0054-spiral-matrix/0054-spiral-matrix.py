class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        inbound = lambda x: 0<=x[0]<len(matrix) and 0<=x[1]<len(matrix[0])
        
        visited = set()
        spiral_nums = []
        move = (0, 1)
        i, j = 0, 0
        while len(spiral_nums)<len(matrix)*len(matrix[0]):
            spiral_nums.append(matrix[i][j])
            visited.add( (i, j) )
            
            new_cell = (i+move[0], j+move[1])
            
            if new_cell not in visited and inbound(new_cell):
                i, j = new_cell
            else:
                move = (move[1], -move[0])
                i, j = i+move[0], j+move[1]
                
        return spiral_nums
                
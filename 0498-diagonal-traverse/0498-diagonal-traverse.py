class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal_nums = len(mat)+len(mat[0])
        diagonal_order = [[] for _ in range(diagonal_nums)]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i+j) % 2 != 0:
                    diagonal_order[i+j].append(mat[i][j])
                else:
                    diagonal_order[i+j].insert(0, mat[i][j])
                
        return sum(diagonal_order, [])

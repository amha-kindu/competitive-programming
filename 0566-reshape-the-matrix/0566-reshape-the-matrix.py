class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if r*c != len(mat)*len(mat[0]):
            return mat
        
        new_mat = []
        mat_row = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(mat_row)==c:
                    new_mat.append(mat_row)
                    mat_row=[]
                mat_row.append(mat[i][j])
                    
        new_mat.append(mat_row)
        return new_mat
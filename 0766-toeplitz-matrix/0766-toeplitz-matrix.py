class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        diag_elems = {}
        
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                diag = row_idx-col_idx
                if diag in diag_elems:
                    diag_elems[diag].add( matrix[row_idx][col_idx] )
                else:
                    diag_elems[diag] = set( [ matrix[row_idx][col_idx] ] )
        
        for elem in diag_elems.values():
            if len(elem)>1:
                return False
            
        return True
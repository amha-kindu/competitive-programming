class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_len = len(matrix[0])
        left = 0
        right = len(matrix)*col_len-1
        while right >= left:
            mid = (right + left) // 2
            
            mid_row = mid // col_len
            mid_col = mid % col_len
            
            left_row = left // col_len
            left_col = left % col_len
            
            right_row = right // col_len
            right_col = right % col_len
            
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid+1
            else:
                right = mid-1
                
        return False
            
            
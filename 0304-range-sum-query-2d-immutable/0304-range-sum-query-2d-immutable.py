class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum2D = [[0 for _ in range(len(matrix[0])+1)]]
        for i in range(len(matrix)):
            temp = [0]
            for j in range(len(matrix[0])):
                temp.append(matrix[i][j])
            self.prefixSum2D.append(temp)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.prefixSum2D[i+1][j+1] = self.prefixSum2D[i][j+1]+self.prefixSum2D[i+1][j]+matrix[i][j] - self.prefixSum2D[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum2D[row2+1][col2+1] + self.prefixSum2D[row1][col1] - \
    self.prefixSum2D[row2+1][col1]-self.prefixSum2D[row1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
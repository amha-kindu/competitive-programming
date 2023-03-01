class Solution:
    def getRow(self, rowIndex: int, row=[]) -> List[int]:
        if rowIndex==-1:
            return row
        
        newRow = [1 for _ in range(len(row)+1)]
        for i in range(1, len(row)):
            newRow[i] = row[i] + row[i-1]
        
        return self.getRow(rowIndex-1, newRow)
            
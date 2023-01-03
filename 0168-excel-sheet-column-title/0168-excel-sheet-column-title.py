class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        excelColumnTitle = ''
        while columnNumber > 0:
            temp = (columnNumber -1)% 26
            excelColumnTitle = chr(temp + 65)+excelColumnTitle
            
            columnNumber = (columnNumber-1) // 26
        return excelColumnTitle
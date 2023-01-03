class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletedColumns = set()
        
        for str_index in range(1, len(strs)):
            for chr_index in range(len(strs[0])):
                if chr_index in deletedColumns:
                    continue
                if strs[str_index][chr_index] < strs[str_index-1][chr_index]:
                    deletedColumns.add(chr_index)
                    
        return len(deletedColumns)
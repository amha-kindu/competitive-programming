class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        indices = {}
        for index in range(len(nums)):
            indices[nums[index]]=index
            
        for operation in operations:
            nums[indices[operation[0]]] = operation[1]
            indices[operation[1]]=indices[operation[0]]
        
        return nums
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = set()
        
        for num in nums:
            if num in single_num:
                single_num.remove(num)
            else:
                single_num.add(num)
                
        return single_num.pop()
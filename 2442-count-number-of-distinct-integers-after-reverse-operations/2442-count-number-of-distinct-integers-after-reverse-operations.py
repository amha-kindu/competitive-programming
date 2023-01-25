class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reverse_op_nums = []
        for num in nums:
            temp = str(num)
            reverse_op_nums.append(
                int( temp )
            )
            reverse_op_nums.append(
                int( temp[::-1] )
            )
        return len(set(reverse_op_nums))
class Solution:
    def findComplement(self, num: int) -> int:     
        return num ^ (2 ** int.bit_length(num) - 1)

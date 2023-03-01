class Solution:
    def findBinaryString(self, n):
        if n == 1:
            return '0'
        binarySub = self.findBinaryString(n-1)
        inverted = binarySub.replace('1', '2').replace('0', '1').replace('2', '0')

        return binarySub+'1'+inverted[::-1]
    
    def findKthBit(self, n: int, k: int) -> str:
        return self.findBinaryString(n)[k-1]
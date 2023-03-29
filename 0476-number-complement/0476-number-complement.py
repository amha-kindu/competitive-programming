class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num)[2:])
        for i in range(len(binary)):
            binary[i] = str((int(binary[i])+1) % 2)
        return int(''.join(binary), 2)

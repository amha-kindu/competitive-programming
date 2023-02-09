class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        
        symbol_val = {
            '-': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        prev = '-'
        for char in s:
            if symbol_val[prev] >= symbol_val[char]:
                number += symbol_val[char]
            else:
                number += symbol_val[char] - 2*symbol_val[prev]
            
            prev = char
            
                
        return number
            
            
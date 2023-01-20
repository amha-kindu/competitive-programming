class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        sum_digits = []
        for dig_idx in range(len(digits)-1, -1, -1):
            digit_sum = carry + digits[dig_idx]
            
            carry = digit_sum // 10
            sum_digits.insert(0, digit_sum % 10)
            
        if carry != 0:
            sum_digits.insert(0, carry)
        
        return sum_digits
            
            
class Solution:
    def multiply_(self, num, digit):
        result, digit, carry = '', int(digit), 0
        
        for n in reversed(num):
            m = carry + int(n)*digit
            result = str(m % 10) + result
            carry = m // 10
            
        return result if carry == 0 else str(carry)+result
    
    def add(self, x, y):
        if len(x)<len(y): x, y = y, x
        carry, result, n = 0, '', len(x)
        for i in range(len(x)):
            temp = carry + int(x[n-i-1]) 
            if i <= len(y)-1 : temp+=int(y[len(y)-i-1])
            result = str(temp % 10) + result
            carry = temp // 10
            
        return result if carry == 0 else str(carry)+result
    
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2): num1, num2 = num2, num1
        n, m = len(num1), len(num2)
        
        if num1=='0' or num2=='0':    return '0'
            
        result =''
        for i in range(m):
            result = self.add(
                result,
                self.multiply_(num1, num2[m-i-1])+'0'*i
            )
            
        return result
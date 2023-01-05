class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        index_1 = num1.find('+')
        index_2 = num2.find('+')
        
        num1_real, num1_imag = int(num1[:index_1]), int(num1[index_1+1:-1])
        num2_real, num2_imag = int(num2[:index_2]), int(num2[index_2+1:-1])
        
        product_real = num1_real*num2_real - num1_imag*num2_imag
        product_imag = num1_real*num2_imag + num2_real*num1_imag
        
        return str(product_real)+'+'+str(product_imag)+'i'
        
        
class Solution:
    def tribonacci(self, n: int) -> int:
        T_prev = [0, 1, 1]
        T_n = sum(T_prev)
        
        if n<3:
            return T_prev[n]
        
        for i in range(3, n+1):
            T_n = sum(T_prev)
            
            T_prev.pop(0)
            T_prev.append(T_n)
            
        return T_n
        
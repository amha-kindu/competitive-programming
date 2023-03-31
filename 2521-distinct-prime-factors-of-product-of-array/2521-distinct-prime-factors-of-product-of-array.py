class Solution:
    def prime_factors(self, n):
        factors = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        if n > 1:
            factors.add(n)
        return factors

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        answer = set()
        for num in nums: 
            temp = self.prime_factors(num)  
            if not answer:
                answer = temp
            else:
                anwer = answer.update(temp)
        return len(answer)

        
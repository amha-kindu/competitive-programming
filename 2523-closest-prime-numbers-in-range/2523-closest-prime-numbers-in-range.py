class Solution:
    def sievePrimes(self, n):
        is_prime = [1]*(n+1)
        is_prime[0] = is_prime[1] = 0

        i = 2
        while i * i <= n:
            if is_prime[i] == 1:
                j = i * i
                while j <= n:
                    is_prime[j] = 0
                    j += i
            i += 1
        return is_prime

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.sievePrimes(right)
        answer, prev = [-1, -1], None
        for prime_num in range(left, len(primes)):
            if primes[prime_num] == 0:  continue
            if prev:
                if sum(answer)==-2 or answer[-1] - answer[0] > prime_num - prev:
                    answer = [prev, prime_num]
            prev = prime_num
        return answer
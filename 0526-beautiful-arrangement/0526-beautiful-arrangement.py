class Solution:

    def countArrangement(self, n: int) -> int:
        self.beautiful_arrangements = 0
        nums = [i for i in range(1, n+1)]
        
        def computePermutation(num=0, path_len=0):
            if path_len == n:
                self.beautiful_arrangements += 1
                return

            for i in range(n):
                # perform kth bit test0
                ith_bit_off = num & (1 << i) == 0

                index = path_len+1
                if ith_bit_off and (nums[i] % index == 0 or index % nums[i] == 0):
                    computePermutation(num+2**i, path_len+1)
        computePermutation()
        return self.beautiful_arrangements
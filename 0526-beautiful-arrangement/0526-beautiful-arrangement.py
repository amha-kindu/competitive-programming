class Solution:
    def computePermutation(self, nums, n=0, path_len=0):
        len_ = len(nums)
        if path_len == len_:
            self.beautiful_arrangements += 1
            return

        for i in range(len_):
            # perform kth bit test0
            ith_bit_off = n & (1 << i) == 0

            index = path_len+1
            if ith_bit_off and (nums[i] % index == 0 or index % nums[i] == 0):
                self.computePermutation(nums, n+2**i, path_len+1)

    def countArrangement(self, n: int) -> int:
        self.beautiful_arrangements = 0
        self.computePermutation([i for i in range(1, n+1)])
        return self.beautiful_arrangements
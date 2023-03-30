class Solution:
    def computePermutation(self, nums, n=0, path=()):
        len_ = len(nums)
        if len(path) == len_:
            self.permutations.append(path)
            return

        for i in range(len_):
            # perform kth bit test
            ith_bit_off = n & (1 << i) == 0

            if ith_bit_off:
                self.computePermutation(nums, n+2**i, path+(nums[i],))


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.computePermutation(nums)
        return self.permutations
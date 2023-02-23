class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]
        for num in nums:
            temp = self.prefixSum[-1]+num
            self.prefixSum.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
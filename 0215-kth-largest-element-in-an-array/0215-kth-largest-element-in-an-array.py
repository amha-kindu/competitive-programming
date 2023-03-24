class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n <= 1:
            return nums[0]

        pivot = nums[0]

        left, right = [], []
        for i in range(1, n):
            if nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])

        if len(right) + 1 < k:
            return self.findKthLargest(left, k-len(right)-1)
        elif len(right) + 1 > k:
            return self.findKthLargest(right, k)
        else:
            return pivot

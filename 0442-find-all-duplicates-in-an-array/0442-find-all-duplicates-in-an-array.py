class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = set()

        for i in range(n):
            while nums[i] - 1 != i and nums[nums[i]-1] != nums[i]:
                nums[ nums[i] - 1 ], nums[i] = nums[i], nums[ nums[i] - 1 ]

            if nums[i] - 1 != i and nums[nums[i]-1] == nums[i]:
                answer.add(nums[i])

        return list(answer)


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] - 1 != i and nums[i] != -1:
                if nums[ nums[i] - 1 ] != nums[i]:
                    nums[ nums[i] - 1 ], nums[i] = nums[i], nums[ nums[i] - 1 ]
                else:
                    nums[i] = -1

        answer = []
        for i in range(n):
            if nums[i] == -1:
                answer.append(i+1)

        return answer
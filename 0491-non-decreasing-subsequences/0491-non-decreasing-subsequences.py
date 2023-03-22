class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        decreasing_subsequences = set()
        n = len(nums)

        def backtrack(i=0, path=(-float('inf'),)):
            
            if len(path) >= 3:
                decreasing_subsequences.add(path[1:])

            if i >= n:
                return

            for j in range(i, n):
                if nums[j] >= path[-1]:
                    backtrack(j+1, path+(nums[j],))

        backtrack()

        return list(decreasing_subsequences)
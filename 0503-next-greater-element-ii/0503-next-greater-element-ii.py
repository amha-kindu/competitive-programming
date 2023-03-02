class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums += nums
        stack = []
        next_greater = defaultdict(lambda: -1)
        for i in range(n*2):
            while stack and nums[stack[-1]] < nums[i]:
                next_greater[stack.pop()] = nums[i]
            stack.append(i)
        answer = [0 for _ in range(n)]
        for i in range(n):
            answer[i] = next_greater[i]
        return answer
        
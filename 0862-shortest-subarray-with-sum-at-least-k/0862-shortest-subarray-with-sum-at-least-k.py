class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = [0]+nums
        for i in range(1, n+1):
            nums[i] += nums[i-1]
        
        min_len = n + 1
        queue = deque()
        for i in range(n+1):
            # Maintain monotonocity when adding to deque
            while queue and nums[queue[-1]]>=nums[i]:
                queue.pop()
            
            while queue and nums[i] - nums[queue[0]] >= k:
                min_len = min(min_len, i - queue.popleft())
            queue.append(i)

        return min_len if min_len < n+1 else -1
                
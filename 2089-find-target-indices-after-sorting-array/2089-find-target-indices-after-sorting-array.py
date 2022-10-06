class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        answer=[]
        for i in range(len(nums)):
            answer.append(i) if nums[i]==target else None
        return answer
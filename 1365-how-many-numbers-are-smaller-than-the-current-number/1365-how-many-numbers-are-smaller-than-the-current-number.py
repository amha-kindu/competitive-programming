class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        original=nums[::]
        nums.sort()
        answer=[]
        for i in original:
            answer.append(nums.index(i))
        return answer

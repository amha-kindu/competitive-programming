class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num>0:   positives.append(num)
            else:   negatives.append(num)
                
        answer = []
        while positives and negatives:
            answer.append(positives.pop(0))
            answer.append(negatives.pop(0))
        
        return answer
        
        
        
                
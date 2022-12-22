class Solution:
    def twoSum(self, nums, ignore=0):
        count = {}
        answer = set()
        for i in range(len(nums)):
            if i == ignore:
                continue
            count[nums[i]] = count.get(nums[i], 0 ) + 1
            
        for num in count:
            if -nums[ignore]-num in count and -nums[ignore]-num!=num:
                m = sorted( (num, -nums[ignore]-num, nums[ignore]) )
                answer.add( tuple(m) )
                
        return answer
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = set()
        for i in range( len(nums) ):
            answer.update( self.twoSum(nums, i) )
        
        if nums.count(0) >= 3:
            answer.add( (0, 0, 0) )
            
        return list( answer )
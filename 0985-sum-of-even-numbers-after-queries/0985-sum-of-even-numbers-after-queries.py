class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        even_sum = sum( filter(lambda x: x%2==0, nums))
        for query in queries:
            val, index = tuple(query)
            
            was_even = nums[index] % 2 == 0
            nums[index]+=val
            is_even = nums[index] % 2 == 0
            
            if was_even and not is_even:
                even_sum -= nums[index] - val
            elif not was_even and is_even:
                even_sum += nums[index]
            elif was_even and is_even:
                even_sum += val
            
            answer.append(even_sum)
            
        return answer
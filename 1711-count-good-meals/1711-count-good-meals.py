class Solution:
    
    def countPairs(self, deliciousness: List[int]) -> int:
        is2Pwr = lambda n: (ceil(log2(n)) == floor(log2(n)))
        
        meal = {}
        for d in deliciousness: meal[d] = meal.get(d, 0) + 1

        count = 0
        for d in meal:
            if d==0: 
                continue
            if is2Pwr(d): 
                count += meal[d]*(meal[d] - 1) // 2
            m = 2**ceil( log2(d) ) - d
            if m in meal:
                count += meal[d] * meal[m]

        return count % 1000000007
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return int(n > 1 and nums[0] == nums[1])
        even_count = defaultdict(int)
        odd_count = defaultdict(int)
        for i in range(n):
            if i % 2 == 0:
                even_count[nums[i]] += 1
            else:
                odd_count[nums[i]] += 1

        even = [(even_count[x], x) for x in even_count]
        odd= [(odd_count[x], x) for x in odd_count]
        
        even.sort(reverse=True)
        odd.sort(reverse=True)
        if even[0][1] == odd[0][1]:
            even_cng = n - even[0][0] - odd[1][0] if len(odd) > 1 else n // 2
            odd_cng = n - even[1][0] - odd[0][0] if len(even) > 1 else n // 2
            return min(even_cng, odd_cng)
        return n - even[0][0] - odd[0][0]
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        count = defaultdict(int)
        left = 0
        max_fruits = 0
        for right in range(n):
            count[fruits[right]]+=1
            while left < n and len(count.keys()) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    count.pop(fruits[left])
                left += 1
            max_fruits = max(max_fruits, right-left+1)
        return max_fruits
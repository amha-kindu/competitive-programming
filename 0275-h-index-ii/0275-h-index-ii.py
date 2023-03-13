class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        answer = 0
        
        left, right = 0, n
        while right >= left:
            mid = (left + right) // 2
            count = bisect_left(citations, mid)
            if n-count >= mid:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
        
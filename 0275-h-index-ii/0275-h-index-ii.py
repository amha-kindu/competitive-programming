class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        hIndex = 0
        
        left, right = 0, n
        while right >= left:
            h = (left + right) // 2
            count = bisect_left(citations, h)
            
            if n - h >= count:
                hIndex = h
                left = h + 1
            else:
                right = h - 1

        return hIndex
        
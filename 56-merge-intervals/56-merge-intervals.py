class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        
        intervals.sort()
        merged=[]
        for i in range(n):
            if merged and intervals[i][0]<=merged[-1][1]:
                a=intervals[i][1]
                x,y=merged[-1]
                merged.pop()
                y=a if a>y else y
                merged.append([x,y])
            else:
                merged.append(intervals[i])
        return merged
        
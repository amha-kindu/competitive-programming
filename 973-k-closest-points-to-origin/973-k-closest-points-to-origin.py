class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        class Point:
            def __init__(self,x):
                self.x=x[0]
                self.y=x[1]
            def magnitude(self):
                return sqrt(self.x**2+self.y**2)
            def __lt__(self,o):
                return self.magnitude()<o.magnitude()
        g=[]
        for p in points:
            heappush(g,Point(p))
        ans=[]
        for _ in range(k):
            h=heappop(g)
            ans.append([h.x,h.y])
        return ans
            
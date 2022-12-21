class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        filtered_points = list(filter(lambda a: a[0]==x or a[1]==y, points))
        if not filtered_points:  return -1
        
        distance = lambda a: abs(a[0]-x)+abs(a[1]-y)    
        filtered_points = sorted(filtered_points, key = distance)
        
        return points.index(filtered_points[0])
        
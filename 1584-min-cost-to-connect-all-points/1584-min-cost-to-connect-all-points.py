class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pointSet = DisjointSet(len(points))
        distance = lambda x, y: abs(x[0]-y[0]) + abs(x[1]-y[1])
        heap = []
        for i in range(len(points)):
            point = points[i]
            for j in range(i, len(points)):
                if i != j:
                    heappush(heap, (distance(point, points[j]), i, j))
       
        while heap:
            dist, i, j = heappop(heap)
            pointSet.union(i, j, dist)

        return pointSet.getCost(0)

 
class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.cost = [0 for i in range(n)]
    
    def rep(self, x):
        if self.root[x] != x:
            self.root[x] = self.rep(self.root[x])
        return self.root[x]
    
    def getCost(self, x):
        root = self.rep(x)
        return self.cost[root]
     
    def getReps(self):
        return [i for i in range(len(self.root)) if self.root[i]==i]
    
    def areConnected(self, x, y):
        return self.rep(x) == self.rep(y)
    
    def allComponents(self):
        return [self.components(rep) for rep in self.getReps()]

    def components(self, x):
        root = self.rep(x)
        answer = []
        for i in range(len(self.root)):
            if self.rep(i) == root:
                answer.append(i)
        return answer

    def union(self, x, y, cost):
        rootX = self.rep(x)
        rootY = self.rep(y)

        if rootX == rootY:
            return
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
            self.cost[rootX] += self.cost[rootY] + cost

        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
            self.cost[rootY] += self.cost[rootX] + cost
        else:
            self.rank[rootX] += 1
            self.root[rootY] = rootX
            self.cost[rootX] += self.cost[rootY] + cost
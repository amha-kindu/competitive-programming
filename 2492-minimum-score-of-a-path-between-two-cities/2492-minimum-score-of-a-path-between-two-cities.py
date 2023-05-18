class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roadSet = DisjointSet(n)
        for src, dst, weight in roads:
            roadSet.union(src-1, dst-1, weight)
        
        return roadSet.minWeight[roadSet.rep(0)]

class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.minWeight = [float('inf') for i in range(n)]
    
    def rep(self, x):
        if self.root[x] != x:
            self.root[x] = self.rep(self.root[x])
        return self.root[x]
    
    def areConnected(self, x, y):
        return self.rep(x) == self.rep(y)

    def union(self, x, y, weight):
        rootX = self.rep(x)
        rootY = self.rep(y)

        if rootX == rootY:
            self.minWeight[rootX] = min(self.minWeight[rootX], weight)
            return
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
            self.minWeight[rootX] = min(self.minWeight[rootX], self.minWeight[rootY], weight)
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
            self.minWeight[rootY] = min(self.minWeight[rootX], self.minWeight[rootY], weight)
        else:
            self.rank[rootX] += 1
            self.root[rootY] = rootX
            self.minWeight[rootX] = min(self.minWeight[rootX], self.minWeight[rootY], weight)

        
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        streets = DisjointSet(n*m)
        uniqueRep = lambda r, c:    m*r + c
        for i in range(n):
            for j in range(m):
                if i+1 < n and grid[i][j] in [2, 3, 4] and \
                    grid[i+1][j] in [2, 5, 6]:
                    streets.union(
                        uniqueRep(i, j), 
                        uniqueRep(i+1, j)
                    )
                if j+1 < m and grid[i][j] in [1, 4, 6] and \
                    grid[i][j+1] in [1, 3, 5, 6]:
                    streets.union(
                        uniqueRep(i, j), 
                        uniqueRep(i, j+1)
                    )

        return streets.areConnected(
            uniqueRep(0, 0),
            uniqueRep(n-1, m-1)
        )


class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def rep(self, x):
        if self.root[x] != x:
            self.root[x] = self.rep(self.root[x])
        return self.root[x]
    
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

    def union(self, x, y):
        rootX = self.rep(x)
        rootY = self.rep(y)

        if rootX == rootY:
            return
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.rank[rootX] += 1
            self.root[rootY] = rootX
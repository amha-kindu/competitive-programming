class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stoneSet = DisjointSet(len(stones))
        for i in range(len(stones)):
            for j in range(i, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    stoneSet.union(i, j)
        count = 0
        for rep in stoneSet.getReps():
            count += stoneSet.count[rep] - 1

        return count

class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.count = [1 for i in range(n)]
    
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

    def union(self, x, y):
        rootX = self.rep(x)
        rootY = self.rep(y)

        if rootX == rootY:
            return
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
            self.count[rootX] += self.count[rootY]

        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
            self.count[rootY] += self.count[rootX]
        else:
            self.rank[rootX] += 1
            self.root[rootY] = rootX
            self.count[rootX] += self.count[rootY]
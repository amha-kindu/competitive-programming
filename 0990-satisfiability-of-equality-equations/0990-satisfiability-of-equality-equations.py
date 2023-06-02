class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        equals = DisjointSet(26)
        graph = defaultdict(set)
        comps = []
        for equation in equations:
            operator = equation[1:3]
            i, j = ord(equation[0])-97, ord(equation[-1])-97
            if operator == '==':
                equals.union(i, j)
            elif i!=j:
                graph[i].add(j)
                graph[j].add(i)
            else:
                return False
            comps.append( (ord(equation[0])-97, ord(equation[-1])-97) )

        for i, j in comps:
            if equals.areConnected(i, j) and j in graph[i]:
                return False
        return True


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
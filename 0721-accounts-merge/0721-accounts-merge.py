class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = {}
        for account in accounts:
            for i in range(1, len(account)):
                if account[i] not in emails:
                    emails[account[i]] = (len(emails), account[0])

        indices = [0]*len(emails)
        accSet = DisjointSet(len(emails))
        for account in accounts:
            for i in range(1, len(account)):
                if i+1 < len(account):
                    accSet.union(emails[account[i]][0], emails[account[i+1]][0])
                indices[emails[account[i]][0]] = account[i]

        answer = []
        for emailList in accSet.allComponents():
            email = indices[emailList[0]]
            name = emails[email][1]
            temp = [indices[i] for i in emailList]
            temp.sort()
            answer.append([name]+temp)
        return answer
        
        
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

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(lambda: [])
        for p1, p2 in dislikes:
            graph[p2].append(p1)
            graph[p1].append(p2)
        
        self.color = {}
        
        def dfs(person, color=1):
            self.color[person] = color
            for enemy in graph[person]:
                if enemy in self.color:
                    if self.color[enemy] == color:
                        return False
                elif not dfs(enemy, -color):
                    return False
            return True
            
        for i in range(1, n+1):
            if i not in self.color:
                if not dfs(i):
                    return False
         
		 # We found no anomaly, so return True
        return True
        
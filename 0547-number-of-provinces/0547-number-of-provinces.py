class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:                
        count = 0
        visited=set()
        for node in range(len(isConnected)):
            if node not in visited:
                count += 1
            # Perform dfs
            frontier=[node]
            while len(frontier) > 0:
                next_=frontier.pop(0)
                visited.add(next_)

                for neighbor in range(len(isConnected[0])):

                    if neighbor not in visited and isConnected[next_][neighbor] == 1:
                        frontier.append(neighbor)
        
        return count
            
        

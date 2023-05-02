class Solution:
    def nextCells(self, i, j, grid):
        n, m = len(grid), len(grid[0])
        answer = []
        if i+1 < n and grid[i+1][j] == '.': answer.append((i+1, j))
        if i-1 > -1 and grid[i-1][j] == '.': answer.append((i-1, j))
        if j+1 < m and grid[i][j+1] == '.': answer.append((i, j+1))
        if j-1 > -1 and grid[i][j-1] == '.': answer.append((i, j-1))
        return answer
        
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        isExit = lambda i, j: (i, j) != tuple(entrance) and maze[i][j] == '.' and (i+1 >= n or j+1 >= m or i-1 < 0 or j-1 < 0)
        nextCells = lambda i: []

        frontier = [tuple(entrance)]
        visited = set()
        depth = 0
        while frontier:
            for _ in range(len(frontier)):
                cell = frontier.pop(0)
                
                if isExit(cell[0], cell[1]):
                    return depth

                for neighbor in self.nextCells(cell[0], cell[1], maze):
                    if neighbor not in visited:
                        frontier.append(neighbor)
                        visited.add(neighbor)

            depth += 1

        return -1
                

        
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        inbound = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        island_1 = set()
        def dfs(r, c):
            island_1.add((r, c))
            next_cells = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for i, j in next_cells:
                if (i, j) not in island_1 and inbound(i, j) and grid[i][j]==1:
                    dfs(i, j)
        land = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land = (i, j)
                    break
            if land:    break

        dfs(land[0], land[1])
        frontier = list(island_1)
        visited = island_1
        depth = 0
        while frontier:
            for _ in range(len(frontier)):
                r, c = frontier.pop(0)
                if  grid[r][c] == 1 and depth > 0:
                    return depth-1

                next_cells = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for i, j in next_cells:
                    if (i, j) not in visited and inbound(i, j):
                        frontier.append((i, j))
                        visited.add((i, j))
 
            depth += 1
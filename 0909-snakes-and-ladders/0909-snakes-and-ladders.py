class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def numToCoord(num):
            r = (num - 1) // n
            c = (num - 1) % n
            if r % 2:
                c = n - 1 - c
            return [r, c]

        frontier = [(1, 0)]
        visited = set()
        while frontier:
            num, depth = frontier.pop(0)

            if num == n**2:
                return depth

            for i in range(1, 7):
                nextNum = min(n**2, num + i)
                r, c = numToCoord(nextNum)
                if board[r][c] != -1:
                    nextNum = board[r][c]
                if nextNum not in visited:
                    visited.add(nextNum)
                    frontier.append((nextNum, depth+1))
        return -1
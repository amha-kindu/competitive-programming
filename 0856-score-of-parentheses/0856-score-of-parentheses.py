class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score, depth = 0, 0
        stack = []
        i = 0
        while i < len(s):
            moved = False
            char = s[i]
            if char == '(':
                depth += 1
                stack.append('(')
            else:
                score += 2 ** (depth-1)
                while stack and i < len(s) and s[i]==')':
                    stack.pop()
                    depth -= 1
                    moved = True
                    i += 1
            i += 1 if not moved else 0

        return score

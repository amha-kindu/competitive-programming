class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}
        for i in range(len(s)):
            last_occur[s[i]] = i
        
        stack = []
        visited = set()
        for i in range(len(s)):
            char = s[i]
            if char not in visited:
                while stack and char < stack[-1] and i < last_occur[stack[-1]]:
                    visited.remove(stack.pop())
        
                stack.append(char)
                visited.add(char)

        return ''.join(stack)
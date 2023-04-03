class Solution:
    @lru_cache(None)
    def minSteps(self, n: int, screen=1, clipboard=1) -> int:
        if screen >= n:
            if n == 1:
                return 0
            elif screen == n:
                return 1
            else:
                return float('inf')
        # Copy
        if screen != clipboard:
            choice2 = self.minSteps(n, screen, screen) + 1
        else:
            choice2 = float('inf')
        
        # Paste
        choice1 = self.minSteps(n, screen+clipboard, clipboard) + 1


        return min(choice1, choice2)
        

        

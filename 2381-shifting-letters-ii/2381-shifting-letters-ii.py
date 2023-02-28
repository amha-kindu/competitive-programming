class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        updates = [0]*n
        for start, end, direction in shifts:
            direction = direction if direction else -1

            updates[start] += direction
            if end+1<n:
                updates[end+1] -= direction
        
        for i in range(1, n):
            updates[i] += updates[i-1]
        
        ans = ''
        for i in range(n):
            next_ = ord(s[i]) + updates[i]
            if next_ > 122:
                next_ = (next_ - 97) % 26 + 97
            elif next_ < 97:
                next_ = 122 - (96-next_) % 26
            ans+=chr(next_)

        return ans


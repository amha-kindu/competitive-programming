class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        answer = [0, float('inf')]
        t_count = Counter(t)
        window = defaultdict(int)
        lacks = len(t_count)
        
        left= 0
        for right in range(n):
            window[s[right]] += 1
            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                lacks -= 1
            while lacks == 0:
                if answer[1]-answer[0]+1 > right-left+1:
                    answer = [left, right]
                window[s[left]]-=1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    lacks += 1
                left+=1
        left, right = answer
        return s[left: right+1] if right!=float('inf') else ''
            

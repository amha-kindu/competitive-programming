class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s2), len(s1)
        set_1 = Counter(s1)
    
        window = Counter(s2[:m])
        left, right = 0, m-1
        while right < n:
            if window  == set_1:
                return True

            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                window.pop(s2[left])
            left += 1

            if right+1<n:
                window[s2[right+1]] = window.get(s2[right+1], 0) + 1
            right += 1
           

        return False

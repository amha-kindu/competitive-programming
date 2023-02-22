class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        ans_ptr = 0
        while left < len(chars):
            right = left
            while right < len(chars) and chars[right]==chars[left]:
                right += 1
            
            chars[ans_ptr] = chars[left]
            if right-left > 1 and ans_ptr+1 < len(chars):
                m = str(right-left)
                for c in m:
                    chars[ans_ptr+1] = c
                    ans_ptr += 1
            ans_ptr += 1
            
            if right < ans_ptr:
                left = ans_ptr
            else:
                left = right

        return ans_ptr
            
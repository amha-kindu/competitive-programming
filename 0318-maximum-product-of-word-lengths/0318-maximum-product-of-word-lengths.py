class Solution:
    def maxProduct(self, words: List[str]) -> int:

        def get_number(s):
            n = 0
            for char in s:
                i = ord(char) - 97 
                # perform kth bit test
                ith_bit_off = n & (1 << i) == 0
                if ith_bit_off:
                    n += 2 ** i
            return n

        max_len = 0
        
        words_num = []
        for word in words:
            words_num.append( (get_number(word), len(word)) )

        for num_1, len_1 in words_num:
            for num_2, len_2 in words_num:
                if num_1 & num_2 == 0:
                    max_len = max(max_len, len_1*len_2)
        return max_len
        

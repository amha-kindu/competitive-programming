class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1 and s[0].isdigit():
            return ''
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ''
                while stack[-1]!='[':
                    substr = stack.pop()+substr
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num)*substr)

        return ''.join(stack)
                

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        answer = ''
        path = path.split('/')
        for dir in path:
            if dir == '..' and stack:
                stack.pop()
            elif dir != '..' and dir!='.' and dir!='':
                stack.append(dir)

        return '/'+'/'.join(stack)

            

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_dir = {}
        
        for path in paths:
            temp = path.split(' ')
            directory, files = temp[0], temp[1:]
            for file in files:
                temp = file.split('(')
                file_name, content = temp[0], temp[1][:-1]
                
                if content not in content_to_dir:
                    content_to_dir[content] = []
                    
                content_to_dir[content].append( directory+'/'+file_name )
                
        answer=[]
        for v in content_to_dir.values():
            if len(v)>=2:
                answer.append(v)
        return answer
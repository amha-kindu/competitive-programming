class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        decommented_source=[]
        multiline = False
        prev_str = ''
        answer = []
        
        ml_stack = []
        sl_stack = []

        for line in source:
            new_line = ''
            i = 0
            while i < len(line):
                char = line[i]
                char += line[i+1]if i+1<len(line) else ''
                
                is_code = len(ml_stack)==0 and len(sl_stack)==0
                
                if char=='//' and is_code:
                    sl_stack.append(i)
                    i+=2
                elif char=='/*' and is_code:
                    ml_stack.append(i)
                    i+=2
                elif char == '*/' and len(sl_stack)==0:
                    if ml_stack:
                        ml_stack.pop()
                        i+=2
                    else:
                        new_line += line[i]
                        i+=1
                        
                else:
                    new_line += line[i] if is_code else ''
                    i+=1
                                        
            sl_stack=[]
            
            if len(ml_stack)>0:
                prev_str += new_line
            elif prev_str+new_line:
                answer.append( prev_str+new_line )
                prev_str=''
                
        return answer
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            if len(token)==1 and ord(token)<48:
                op1=operands.pop()
                op2=operands.pop()
                if token == '*':
                    result = op1*op2
                elif token == '/':
                    result = int(op2/op1)
                elif token == '+':
                    result = op1+op2
                else:
                    result = op2-op1
                operands.append(result)
            else:
                operands.append(int(token))
                
        return operands.pop()
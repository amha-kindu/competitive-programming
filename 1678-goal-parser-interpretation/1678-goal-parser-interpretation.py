class Solution:
    def interpret(self, command: str) -> str:
        parsed = ''
        for i in range(len(command)):
            if i+1<len(command) and command[i] == '(' and command[i+1]==')':
                parsed +='o'
            elif command[i]!=')' and command[i]!='(':
                parsed +=command[i]
        return parsed
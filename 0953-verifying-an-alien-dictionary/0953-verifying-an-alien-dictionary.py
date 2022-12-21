class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        numeric_order = {}
        for i in range(len(order)): numeric_order[order[i]] = i

        def greater(x, y):
            if(x==y):   return False
            m = len(x) if len(x) > len(y) else len(y)
                
            for i in range(m):
                if i>=len(x):   return False
                if i>=len(y):   return True
                
                if numeric_order[x[i]] < numeric_order[y[i]]:  
                    return False
                elif numeric_order[x[i]] > numeric_order[y[i]]:
                    return True
            return True

        for j in range(len(words)-1):
            if greater(words[j], words[j+1]):
                return False
        return True
            
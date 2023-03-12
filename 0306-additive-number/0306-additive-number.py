class Solution:
    def isAdditiveNumber(self, num: str, i=0, path=[]) -> bool:
        n = len(num)
        
        if len(path) > 3:
            path.pop(0)

        if i >= n:
            if len(path) >= 3:  return path[-3]+path[-2] == path[-1]
            else:   return False
        
        if len(path) >= 3 and path[-3]+path[-2] != path[-1] \
            or len(num) < 3:
            return False

        for j in range(i, n):
            temp = num[i:j+1]
            if (temp[0]!='0' or int(temp)==0) and self.isAdditiveNumber(num, j+1, path+[int(temp)]):
                    return True
        return False
        
        

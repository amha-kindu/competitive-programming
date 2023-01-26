class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = [i for i in range(1, n+1)]
        
        current = 0
        while len(array) > 1:
            new_idx = (current+k-1)%len(array)
            array.pop(new_idx)
            current = new_idx
            
        return array.pop()
                
            
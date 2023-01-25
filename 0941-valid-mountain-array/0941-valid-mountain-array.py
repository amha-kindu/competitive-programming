class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: 
            return False

        for i in range(1, len(arr)-1):
            
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                for m in range(i-1):
                    if arr[m]>=arr[m+1]:
                        return False
                    
                for m in range(i, len(arr)-1):
                    if arr[m]<=arr[m+1]:
                        return False
                
                return True
                    
        return False
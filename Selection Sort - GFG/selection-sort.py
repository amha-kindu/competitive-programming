#User function Template for python3

class Solution:    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            max_idx = 0
            for j in range(n-i):
                max_idx = j if arr[j]>arr[max_idx] else max_idx
            
            arr[n-i-1], arr[max_idx] = arr[max_idx], arr[n-i-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
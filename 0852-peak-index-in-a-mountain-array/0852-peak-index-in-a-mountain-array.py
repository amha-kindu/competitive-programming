class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n-1
        while right >= left:
            mid = (right + left) // 2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        
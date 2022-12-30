class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right = m-1, n-1
        head = m+n-1
        while left>=0 or right>=0:
            left_val = nums1[left] if left>=0 else -float('inf')
            right_val = nums2[right] if right>=0 else -float('inf')
            
            if left_val < right_val:
                nums1[head] = right_val
                right-=1
            else:
                nums1[head] = left_val
                left-=1
            
            head -= 1

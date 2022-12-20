class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        queue = []
        l, r= 0, 0
        while(l<m+n):
            nums1[l] = float('inf') if l >= m else nums1[l]
            w = nums2[r] if r<n else float('inf')
            if queue and queue[0] <= nums1[l] and queue[0] < w:
                queue.append(nums1[l]) if nums1[l]!=float('inf') else None
                nums1[l] = queue.pop(0)  
            elif(w < nums1[l]):
                queue.append(nums1[l]) if nums1[l]!=float('inf') else None
                nums1[l] = nums2[r]
                r+=1
            l+=1

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [-1]
        max_ = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            max_ = max(max_, arr[i])
            answer.insert(0, max_)
        return answer
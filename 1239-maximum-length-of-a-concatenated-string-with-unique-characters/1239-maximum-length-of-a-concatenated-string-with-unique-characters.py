class Solution:

    def maxLength(self, arr: List[str], i=0, path=set()) -> int:
        n = len(arr)

        if i >= n:
            return len(path)

        temp = set(arr[i])

        valid = len( path.intersection(temp) ) == 0 and len(temp) == len(arr[i])

        choice1 = self.maxLength(arr, i+1, path.union(set(arr[i])))
        choice2 = self.maxLength(arr, i+1, path)

        if not valid:   choice1 = 0

        return max(choice1, choice2)     
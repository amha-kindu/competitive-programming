class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        
        next_stack, prev_stack = [], []
        next_smaller, prev_smaller = defaultdict(lambda: n), defaultdict(lambda: -1)
        for i in range(n):
            while next_stack and arr[next_stack[-1]] >= arr[i]:
                next_smaller[next_stack.pop()] = i

            while prev_stack and arr[prev_stack[-1]] > arr[n-i-1]:
                prev_smaller[prev_stack.pop()] = n-i-1

            next_stack.append(i)
            prev_stack.append(n-i-1)

        count = 0
        for i in range(n):
            count += arr[i]*(i-prev_smaller[i]) * (next_smaller[i]-i)
        return count%1000000007

        
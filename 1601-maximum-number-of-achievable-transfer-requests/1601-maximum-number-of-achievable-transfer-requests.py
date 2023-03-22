class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)

        def countValidRequests(buildings=[0]*n, i=0, cnt=0):
            if i >= m:
                if buildings.count(0) == n:
                    return cnt
                else:
                    return 0
            
            origin, destination = requests[i]

            # Reject the current request
            choice1 = countValidRequests(buildings, i+1, cnt)

            buildings[origin] -= 1
            buildings[destination] += 1

            # Accept the current request
            choice2 = countValidRequests(buildings, i+1, cnt+1)

            buildings[origin] += 1
            buildings[destination] -= 1

            return max(choice1, choice2)

        return countValidRequests()
        


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n, MAX_DIST = len(trips), 1001
        passengers = [0]*MAX_DIST

        for pass_count, origin, dest in trips:
            passengers[origin] += pass_count
            passengers[dest] -= pass_count

        for i in range(1, MAX_DIST):
            passengers[i] += passengers[i-1]

        for pass_count in passengers:
            if pass_count > capacity:
                return False
        return True
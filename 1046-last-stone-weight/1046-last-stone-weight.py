class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            rock1 = heapq._heappop_max(stones)
            rock2 = heapq._heappop_max(stones)
            if rock1 != rock2:
                stones.append(rock1 - rock2)
                heapq._siftdown_max(stones, 0, len(stones)-1)
            
        return sum(stones)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins=0
        while len(piles)>0:
            coins+=piles[-2]
            piles.pop()
            piles.pop()
            piles.pop(0)
        return coins
        
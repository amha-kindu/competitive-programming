class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stash = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            change = bill - 5
            stash[bill] += 1

            chang_20 = min(change // 20, stash[20]) 
            stash[20] -= chang_20
            change -= chang_20 * 20

            chang_10 = min(change // 10, stash[10]) 
            stash[10] -= chang_10
            change -= chang_10 * 10

            chang_5 = min(change // 5, stash[5]) 
            stash[5] -= chang_5
            change -= chang_5 * 5
            
            if change > 0:
                return False

        return True
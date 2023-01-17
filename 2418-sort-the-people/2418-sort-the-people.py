class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(names)):
            min_idx = 0
            for j in range(len(names)-i):
                if heights[j] < heights[min_idx]:
                    min_idx = j
            
            names[-1-i], names[min_idx] = names[min_idx], names[-1-i]
            heights[-1-i], heights[min_idx] = heights[min_idx], heights[-1-i]
        
        return names
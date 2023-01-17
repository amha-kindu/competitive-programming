class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for j in range(1, len(names)):
            for i in range(j, 0, -1):
                if heights[i]>heights[i-1]:
                    names[i-1], names[i] = names[i], names[i-1]
                    heights[i-1], heights[i] = heights[i], heights[i-1]
        
        return names
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        while True:
            swapped = False
            for i in range(len(names)-1):
                if heights[i]<heights[i+1]:
                    names[i], names[i+1] = names[i+1], names[i]
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    swapped=True
            
            if not swapped:
                break
            
        return names
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        
        getValue=lambda s: image[s[0]][s[1]]
        def neighbors(cell):
            cellColor=getValue(cell)
            nbr = []
            if cell[0]-1 >= 0 and getValue( (cell[0]-1,cell[1]) ) == cellColor:
                nbr+=[(cell[0]-1,cell[1])]
            if cell[0]+1 < n and getValue( (cell[0]+1,cell[1]) ) == cellColor:
                nbr+=[(cell[0]+1,cell[1])]
            if cell[1]-1 >= 0 and getValue( (cell[0],cell[1]-1) ) == cellColor:
                nbr+=[(cell[0],cell[1]-1)]
            if cell[1]+1 < m and getValue( (cell[0],cell[1]+1) ) == cellColor:
                nbr+=[(cell[0],cell[1]+1)]
            return nbr
                      
        start=(sr,sc)
        if getValue(start) == color:
            return image

        frontier=[start]
        visited=set()
        while len(frontier)>0:
            pixel=frontier.pop(0)
            visited.add(pixel)
            for cell in neighbors(pixel):
                if cell not in visited:
                    frontier.append(cell)
            image[pixel[0]][pixel[1]]=color
            
        return image
            
           
        
class Solution:
    
    def isCloser(self, point_1, point_2, reference):
        distance_1 = (point_1[0]-reference[0])**2 +(point_1[1]-reference[1])**2
        distance_2 = (point_2[0]-reference[0])**2 +(point_2[1]-reference[1])**2

        return distance_1 < distance_2

    def queensAttacktheKing(self, queens, king):
        origin = [float('inf'), float('inf')]
        attackQueens = {
            'top':origin, 'down':origin, 'left':origin, 'right':origin,
            'diag_up':origin, 'diag_down':origin, 'diag_left':origin, 'diag_right':origin
        }

        for queen in queens:
            on_left = queen[0]==king[0] and queen[1]<king[1]
            on_right = queen[0]==king[0] and queen[1]>king[1]
            on_top = queen[1]==king[1] and queen[0]<king[0]
            on_bottom = queen[1]==king[1] and queen[0]>king[0]


            if on_left and self.isCloser(queen, attackQueens['left'], reference = king):
                attackQueens['left'] = queen
            elif on_right and self.isCloser(queen, attackQueens['right'], reference = king):
                attackQueens['right'] = queen
            elif on_top and self.isCloser(queen, attackQueens['top'], reference = king):
                attackQueens['top'] = queen
            elif on_bottom and self.isCloser(queen, attackQueens['down'], reference = king):
                attackQueens['down'] = queen
                
            if abs(queen[0]-king[0])!=abs(queen[1]-king[1]):
                continue
                
            on_diag_left = queen[1]<king[1] and queen[0]<king[0]
            on_diag_up = queen[1]>king[1] and queen[0]<king[0]
            on_diag_down = queen[0]>king[0] and queen[1]<king[1]
            on_diag_right = queen[1]>king[1] and queen[0]>king[0]

            if on_diag_left and self.isCloser(queen, attackQueens['diag_left'], reference = king):
                attackQueens['diag_left'] = queen
            elif on_diag_right and self.isCloser(queen, attackQueens['diag_right'], reference = king):
                attackQueens['diag_right'] = queen
            elif on_diag_up and self.isCloser(queen, attackQueens['diag_up'], reference = king):
                attackQueens['diag_up'] = queen
            elif on_diag_down and self.isCloser(queen, attackQueens['diag_down'], reference = king):
                attackQueens['diag_down'] = queen
                
        print(attackQueens)

        return list( filter(lambda a: a!=origin, attackQueens.values() ) )

        
            
            
class Solution:
    def racecar(self, target: int) -> int:
        frontier = [(0, 1)]
        visited = set([(0, 1)])
        depth = 0
        while frontier:
            for _ in range(len(frontier)):
                pos, velocity = frontier.pop(0)
                
                if pos == target:
                    return depth

                # Always consider moving the car in the direction it is already going
                frontier.append((pos + velocity, 2 * velocity))
                
                # Only consider changing the direction of the car if one of the following conditions is true
                #   i.  The car is driving away from the target.
                #   ii. The car will pass the target in the next move.  
                if (pos + velocity > target and velocity > 0) or\
                     (pos + velocity < target and velocity < 0):

                    frontier.append((pos, -velocity / abs(velocity)))
            depth += 1
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        arrival_time = {}
        for i in range(n):
            arrival_time[position[i]] = (target-position[i]) / speed[i]

        position.sort()
        mono= []

        for i in range(n):
            while mono and mono[-1] <= arrival_time[position[i]]:
                mono.pop() 
            mono.append(arrival_time[position[i]])
        return len(mono)
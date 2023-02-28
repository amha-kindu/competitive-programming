class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = []
        for i in range(len(tickets)):
            queue.append(i)
            
        time = 1
        while tickets[k] > 0:
            for _ in range(len(queue)):
                i = queue.pop(0)
                tickets[i] -= 1
                if tickets[i] >= 1:
                    queue.append(i)

                if tickets[k] > 0:
                    time += 1
                else:
                    break
        return time

        

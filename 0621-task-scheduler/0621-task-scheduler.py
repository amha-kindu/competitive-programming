class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[]
        totalTime = 0
        for i in set(tasks): heappush(count,-tasks.count(i))
        
        queue=deque()
        
        while count or queue:
            if queue and queue[0][1]==totalTime:
                l,_=queue.popleft()
                heappush(count, l)
            if count:
                g = heappop(count)
                if g+1!=0:
                    queue.append((g+1, totalTime+n+1))
            totalTime+=1
        return totalTime
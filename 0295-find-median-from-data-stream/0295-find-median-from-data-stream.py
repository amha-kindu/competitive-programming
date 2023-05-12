class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def balance(self):
        while(len(self.maxHeap) > len(self.minHeap)+1):
            heappush(self.minHeap, -heappop(self.maxHeap))

        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            temp1, temp2 = -heappop(self.maxHeap), -heappop(self.minHeap)
            heappush(self.minHeap, temp1)
            heappush(self.maxHeap, temp2)

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap) + 1:
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
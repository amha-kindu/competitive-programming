class MinStack:

    def __init__(self):
        self.elements=[]
        self.minimum=float('inf')

    def push(self, val: int) -> None:
        self.elements.append(val)
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        removedElem=self.elements.pop()
        if len(self.elements)!=0:
            self.minimum=min(self.elements) if removedElem==self.minimum else self.minimum
        else:
            self.minimum = float('inf')

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
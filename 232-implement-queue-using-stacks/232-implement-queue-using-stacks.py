class MyQueue:

    def __init__(self):
        self.inbox=[]
        self.outbox=[]
    def rearrange(self):
        if len(self.outbox)<1:
            self.outbox=self.inbox[::-1]
            self.inbox=[]

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def pop(self) -> int:
        self.rearrange()    
        return self.outbox.pop()
        

    def peek(self) -> int:
        self.rearrange()
        return self.outbox[-1]
        

    def empty(self) -> bool:
        return not self.inbox and not self.outbox


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
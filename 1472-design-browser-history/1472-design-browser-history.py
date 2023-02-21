class ListNode:
    def __init__(self, val, prev=None, next_=None):
        self.val = val
        self.next = next_
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str) -> None:
        self.current = ListNode(homepage)

    def visit(self, url) -> None:
        new_node = ListNode(url, self.current)
        self.current.next = new_node

        self.current = self.current.next

    def back(self, steps) -> str:
        i = 0
        while self.current.prev and i < steps:
            self.current = self.current.prev
            i += 1
        
        return self.current.val
    
    def forward(self, steps) -> str:
        i = 0
        while self.current.next and i < steps:
            self.current = self.current.next
            i += 1
        
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
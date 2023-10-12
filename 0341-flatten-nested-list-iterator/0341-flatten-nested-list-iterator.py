# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.elements = []
        for item in self.nestedList:
            self._collect(item)
        self.current = 0

    def _collect(self, item):
        if item.isInteger():
            self.elements.append(item.getInteger())
            return
        for elem in item.getList():
            self._collect(elem)
    
    def next(self) -> int:
        if self.current < len(self.elements):
            item = self.elements[self.current]
            self.current += 1
            return item
    
    def hasNext(self) -> bool:
        return self.current < len(self.elements)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
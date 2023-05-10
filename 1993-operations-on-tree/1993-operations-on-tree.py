class LockingTree:

    def __init__(self, parent: List[int]):
        self.tree = defaultdict(lambda: [])
        for i in range(len(parent)):
            self.tree[parent[i]].append(i)

        self.locked = {}
        self.parent = parent

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            self.locked.pop(num)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        nodeIsLocked = num not in self.locked
        noLockedAncestors = True
        i = num
        while i != -1:
            if i in self.locked:
                noLockedAncestors = False
                break
            i = self.parent[i]
        self.lockedDescendants = []
        self.preOrder(num)
        lockedDescendants = len(self.lockedDescendants) > 0

        if nodeIsLocked and noLockedAncestors and lockedDescendants:
            self.locked[num] = user
            for node in self.lockedDescendants:
                self.locked.pop(node)
            return True
        return False
        
    def preOrder(self, node):
        if node in self.locked:
            self.lockedDescendants.append(node)
        for child in self.tree[node]:
            self.preOrder(child)


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
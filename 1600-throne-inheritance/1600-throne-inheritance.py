class ThroneInheritance:

    def __init__(self, kingName: str):
        self.nation = defaultdict(list)
        self.king = kingName
        self.deadKings = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.nation[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deadKings.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.inheritance_order = []
        self.dfs(self.king)
        return self.inheritance_order
    
    def dfs(self, current):
        if current not in self.deadKings:
            self.inheritance_order.append(current)
        for child in self.nation[current]:
            self.dfs(child)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
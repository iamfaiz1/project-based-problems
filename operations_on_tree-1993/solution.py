class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.lockedBy = [ -1 for _ in range(len(self.parent))]
        self.di = {}
        for i,  p in enumerate(parent):
            self.di[p] = self.di.get(p, []) + [i]

    def lock(self, num: int, user: int) -> bool:
        if self.lockedBy[num] != -1:
            return False
        else:
            self.lockedBy[num] = user
            return True

    def unlock(self, num: int, user: int) -> bool:
        if self.lockedBy[num] != user:
            return False
        self.lockedBy[num] = -1
        return True
        

    def upgrade(self, num: int, user: int) -> bool:
        # conditions:
        # 1: node is unlocked:
        if self.lockedBy[num] != -1:
            return False
        
        # 3: no locked ancestors:
        cur = self.parent[num]
        while cur !=-1:
            if self.lockedBy[cur] != -1:
                return False
            cur = self.parent[cur]
        
        # 2: atleast one locked decendent
        flag = False
        
        def dfs(node):
            nonlocal flag
            if node in self.di:
                for child in self.di[node]:
                    if self.lockedBy[child] != -1:
                        flag = True
                    self.lockedBy[child] = -1
                    dfs(child)
        dfs(num)

        if not flag:
            return False
        
        self.lockedBy[num] = user
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
import heapq
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.di = {}
        self.heap = []
        for u, t, p in tasks:
            self.di[t] = (u, p)
            heapq.heappush(
                self.heap, 
                (-p, -t, u)
            )

    def add(self, userId: int, taskId: int, priority: int) -> None:
        log = (-priority, -taskId, userId)
        heapq.heappush(
            self.heap, 
            log
        )
        self.di[taskId] = (userId, priority)


    def edit(self, taskId: int, newPriority: int) -> None:
        # we'll just push new log while not deleting the old one immediately, and lazy delete it when we pop from the heap

        userId, oldPriority = self.di[taskId]
        new_log = (-newPriority, -taskId, userId)

        self.di[taskId] = (userId, newPriority)
        heapq.heappush(
            self.heap,
            new_log
        )

        

    def rmv(self, taskId: int) -> None:
        # again keeping the old log in the heap, and lazy delete it when we pop from the heap
        del self.di[taskId]

    def execTop(self) -> int:
        # lazy deleting
        while self.heap:
            neg_p, neg_t, u = heapq.heappop(self.heap)
            p = -neg_p
            t = -neg_t

            if t not in self.di:
                continue
            
            latest_user, latest_priority = self.di[t]
            if latest_priority != p or u!= latest_user:
                continue
            
            else:
                del self.di[t]
                return u
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
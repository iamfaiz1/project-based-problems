# used stack, heap and dictionary. dictionary is used to keep track of the number of times an element is popped from the stack. The heap is used to get the minimum element in O(log n) time. The stack is used to keep track of the elements in the order they are pushed. The pop operation is O(1) and the getMin operation is O(log n). The space complexity is O(n) where n is the number of elements in the stack.

import heapq
class MinStack:

    def __init__(self):
        self.heap = []
        self.stack = []
        self.di = {}

    def push(self, value: int) -> None:
        self.stack.append(value)
        heapq.heappush(self.heap, value)

    def pop(self) -> None:
        item = self.stack.pop()
        self.di[item] = self.di.get(item, 0) +1

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        while self.heap:
            item = self.heap[0]
            # print(self.st, item)
            if item in self.di and self.di[item]> 0:
                heapq.heappop(self.heap)
                self.di[item] -=1
            else:
                break
        # print(self.stack)
        # print(self.st)
        # print(self.heap)
        return item
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



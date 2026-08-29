# better solution is to use two stacks, one for the actual stack and one for the minimum values. The minimum stack will only store the minimum values, so when we pop from the actual stack, we also pop from the minimum stack if the popped value is equal to the top of the minimum stack. This way, we can get the minimum value in O(1) time.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack or value <= self.minstack[-1]:
            self.minstack.append(value)


    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
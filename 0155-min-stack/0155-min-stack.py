class MinStack:

    def __init__(self):
        self.stack = []
        self.pre_min = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.pre_min) != 0:
            self.pre_min.append(min(self.pre_min[-1],val))
        else:
            self.pre_min.append(val)
        return 

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.pre_min.pop()
        return 
        
    def top(self) -> int:
        top_ele = self.stack[-1]
        return top_ele

    def getMin(self) -> int:
        minn = self.pre_min[-1]
        return minn
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
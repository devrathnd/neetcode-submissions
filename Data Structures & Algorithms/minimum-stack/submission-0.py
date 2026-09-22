class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        stackLen = len(self.stack)
        if stackLen == 0:
            minVal = val
        else:
            minVal = min(val, self.minStack[stackLen - 1])
        
        self.stack.append(val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        del self.stack[-1]
        del self.minStack[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

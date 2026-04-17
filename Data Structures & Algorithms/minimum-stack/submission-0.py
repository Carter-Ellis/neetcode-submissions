class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.length = 0

    def push(self, val: int) -> None:
        self.size += 1
        if self.size > self.length and self.size == 1:
            self.length = 1
            self.stack = [val]
        elif self.size > self.length:
            self.length = self.length * 2
            newStack = [0] * self.length
            for i in range(len(self.stack)):
                newStack[i] = self.stack[i]
            newStack[self.size - 1] = val
            self.stack = newStack
        else:
            self.stack[self.size - 1] = val

    def pop(self) -> None:
        self.size -= 1


    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        minNum = sys.maxsize
        for i in range(self.size):
            minNum = min(self.stack[i], minNum)
        return minNum

class MinStack:

    def __init__(self):
        self.q = deque()
        self.minimum = deque()
        
    def push(self, val: int) -> None:
        self.q.append(val)

        if not self.minimum or self.minimum[-1] >= val:
            self.minimum.append(val)

    def pop(self) -> None:
        val = self.q.pop()

        if val == self.minimum[-1]:
            self.minimum.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        

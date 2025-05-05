class MinStack:
    
    def __init__(self):
        self.stack = []
        self.mins = []
          
    def push(self, val: int) -> None:
        temp = min(self.mins[-1],val) if self.mins else val
        self.mins.append(temp)
        self.stack.append(val)

    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        

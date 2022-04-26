class MinStack:

    def __init__(self):
        self.data = []

        

    def push(self, val: int) -> None:
        self.data.append(val)

        

    def pop(self) -> None:
        self.data.pop()
        

    def top(self) -> int:
        return self.data.pop()
        

    def getMin(self) -> int:
        return (sorted(self.data)[-1])
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
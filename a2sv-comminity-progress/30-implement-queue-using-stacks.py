import copy
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.data: return None
        return self.data.pop()

    def peek(self):
        if not self.data: return None
        return self.data[-1]
    def getLength(self):
        return len(self.data)
     
class MyQueue:

    def __init__(self):
        self.data = Stack()
        self.length = 0
        
    def push(self, x: int) -> None:
        self.data.push(x)
        self.length += 1
        
    def pop(self) -> int:
        data = copy.deepcopy(self.data)
        tempStack = Stack()
        tempLength = 0
        tempTop = data.pop() 
        if not tempTop: return None
        while tempTop and tempLength < self.length:
            tempStack.push(tempTop)
            tempTop = data.pop()
            tempLength+=1
        self.length -= 1
        return tempStack.pop()

    def peek(self) -> int:
        data = copy.deepcopy(self.data)
        tempStack = Stack()
        tempLength = 0
        tempTop = data.pop() 
        if not tempTop: return None
        while tempTop and tempLength < self.length:
            tempStack.push(tempTop)
            tempTop = data.pop()
            tempLength+=1
        return tempStack.pop()

        

    def empty(self) -> bool:
        return not bool(self.length)

# ["MyQueue","push","push","peek","pop","empty"]
# [[],[1],[2],[],[],[]]
q = MyQueue()
print(q.push(1))
print(q.push(2))
print(q.push(3))
print(q.push(4))
print(q.pop())
print(q.push(5))
print("67", q.pop())
print("68", q.pop())
print("69", q.pop())
print("70", q.pop())
# print(q.peek())
# print(q.pop())
# print(q.empty())
# q.peek()
# q.pop()
# q.empty()
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyCircularDeque:

    def __init__(self, k: int):
        self.data = []
        self.MAX_SIZE = k

    def insertFront(self, value: int) -> bool:
        if (len(self.data) ==  self.MAX_SIZE): return False
        self.data = [value] + self.data
        return True
            
    def insertLast(self, value: int) -> bool:
        if (len(self.data) == self.MAX_SIZE): return False
        self.data = self.data + [value] 
        return True
        
    def deleteFront(self) -> bool:
        if not (len(self.data)):return False
        self.data.pop(0)
        return True
        
    def deleteLast(self) -> bool:
        if not (len(self.data)): return False
        self.data.pop(-1)
        return True
        
    def getFront(self) -> int:
        if not (len(self.data)): return -1
        return self.data[0]
        
    def getRear(self) -> int:
        if not (len(self.data)): return -1
        return self.data[-1]
        
    def isEmpty(self) -> bool:
        return not bool(len(self.data))
        
    def isFull(self) -> bool:
        return (len(self.data) == self.MAX_SIZE)
class LinkedNode:
    def __init__(self, data = 0, next = None):
        self.val = data
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if self.head == None: return -1
        current = self.head
        for i in range(index):
            current = current.next
            if current == None: return -1 
        return current.val
    
    def addAtHead(self, val: int):
        if self.head == None:
            self.head = LinkedNode(val)
        else:
            self.head = LinkedNode(val, self.head)
    
    def addAtTail(self, val:int):
        if self.head == None:
            self.head = LinkedNode(val)
        else:
            prev = None
            current = self.head
            while (current != None):
                prev = current
                current = current.next
            prev.next = LinkedNode(val)
    
    def addAtIndex(self, index: int, val: int):
        if self.head == None and index==0:
            self.head = LinkedNode(val)
        elif self.head !=None and index==0:
            self.addAtHead(val)
        elif self.head == None and index !=0:
            return
        else:
            prev = self.head
            current = self.head
            counter = 0
            while (current != None and counter < index):
                counter += 1 
                prev = current
                current = current.next
            if (current == None and counter != index):
                return
            else:
                prev.next = LinkedNode(val, current)
    
    def deleteAtIndex(self, index:int):
        if self.head == None:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            current = self.head
            counter = 0
            while (current != None and counter < index):
                counter += 1 
                prev = current
                current = current.next
            if (current == None):
                return
            else:
                prev.next = current.next
            
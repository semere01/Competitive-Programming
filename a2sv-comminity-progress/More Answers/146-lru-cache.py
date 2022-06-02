
class Node:
    prev = None
    next = None 
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(None) # add here
        self.tail = Node(None) # remove here
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key: int, value: int) -> None:
        try: # if key exists
            valNode = self.cache.pop(key)
            self.remove(valNode)
            valNode.val = value
            self.add(valNode)
            self.cache[key] = valNode

        except: # if key doesn't exist
            if len(self.cache) == self.capacity:
                trash = self.tail.prev
                self.cache.pop(trash.key)
                self.remove(trash)
            newNode = Node(key, value)
            self.add(newNode)
            self.cache[key] = newNode
    
    def get(self, key: int) -> int:
        try:
            valNode = self.cache[key]
            self.remove(valNode)
            self.add(valNode)
            return (valNode.val)
        except:
            return -1
    
    def add(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node
    
    def remove(self, node):
        nodePrev = node.prev
        nodeNext = node.next
        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev



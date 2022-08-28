class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.content = None
        self.number = None
        pass





tCount = int(input())
for t in range(tCount):
    r, f = [int (i) for i in input().split(" ")]
    friendRooms = [int (i) for i in input().split(" ")]
    nodeMap = {}
    corridors = []
    for i in range(r-1):
        a, b = [int (i) for i in input().split(" ")]
        corridors.append((a, b))
        # corridors.append(a)
        # corridors.append(b)
    
    for (n1, n2) in corridors:
        if n1 not in nodeMap:
            nodeMap[n1] = Node()
        if n2 not in nodeMap:
            nodeMap[n2] = Node()
        

    






    
    

        
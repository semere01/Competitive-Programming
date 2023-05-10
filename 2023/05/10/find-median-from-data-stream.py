class MedianFinder:

    def __init__(self):
        self.topHeap = []
        self.bottomHeap = []
    
    def addNum(self, val):
        if len(self.topHeap) == 0:
            self.topHeap = [val]
            return
        topPop = self.topHeap[0]
        
        if len(self.bottomHeap) == 0:
            if topPop < val:
                heappop(self.topHeap)
                heappush(self.topHeap, val)

                self.bottomHeap = [-topPop]
                return
            else:
                self.bottomHeap = [-val]
                return
        bottomPop = self.bottomHeap[0] * -1

        if topPop < val and bottomPop < val:
            heappush(self.topHeap, val)
        elif topPop > val and bottomPop > val:
            heappush(self.bottomHeap, -val)
        elif topPop >= val and bottomPop <= val:
            heappush(self.bottomHeap, -val)
        else:
            print(val)
            print(self.topHeap)
            print(self.bottomHeap)
            print("logical error")
        
        # if top heap is too big
        if (len(self.topHeap) - len(self.bottomHeap)) > 1:
            topPop = heappop(self.topHeap)
            heappush(self.bottomHeap, -topPop)
        # if bottom heap is too big
        elif (len(self.topHeap) - len(self.bottomHeap) < -1):
            bottomPop = heappop(self.bottomHeap) * -1
            heappush(self.topHeap, bottomPop)

    def findMedian(self) -> float:
        if len(self.topHeap) == 0:
            return None
        elif len(self.bottomHeap) == 0:
            return self.topHeap[0]
        elif (len(self.topHeap) == len(self.bottomHeap)):
            return (self.topHeap[0] - self.bottomHeap[0])/2
        elif (len(self.topHeap) > len(self.bottomHeap)):
            return self.topHeap[0]
        else: 
            return self.bottomHeap[0] * -1
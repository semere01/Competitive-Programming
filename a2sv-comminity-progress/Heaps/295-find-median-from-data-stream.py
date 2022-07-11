from heapq import *


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
                heapreplace(self.topHeap, val)
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
        
        
        if (len(self.topHeap) - len(self.bottomHeap)) > 1:
            topPop = heappop(self.topHeap)
            heappush(self.bottomHeap, -topPop)
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

        
        
medianFinder = MedianFinder();
medianFinder.addNum(1);    # arr = [1]
medianFinder.addNum(2);    # arr = [1, 2]
print(medianFinder.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)    # arr[1, 2, 3]
print(medianFinder.findMedian()); # return 2.0






#  a = [2,1,3]

        

    # def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
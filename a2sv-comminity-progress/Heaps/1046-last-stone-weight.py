class Solution:
    def lastStoneWeight(self, stones):  # : List[int]) -> int:
        heap = MaxHeap(stones)
        while(len(heap.data) > 1):
            s = abs(heap.pop() - heap.pop())
            if s:
                heap.add(s)

        if (len(heap.data)):
            return heap.data[0]
        return 0

class MaxHeap:
    def __init__(self, arr):
        self.data = []
        for val in arr:
            self.add(val)

    def add(self, val):
        if len(self.data) == 0:
            self.data = [val]
            return
        self.data.append(val)
        self.bubbleUp(len(self.data)-1)

    def isValidHeap(self) -> bool:
        nums = self.data
        n = len(nums)
        for i in range(n):
            m = i * 2
            num = nums[i]
            if m + 1 < n:
                if num < nums[m + 1]:
                    return False
            if m + 2 < n:
                if num < nums[m + 2]:
                    return False
        return True

    def pop(self):
        if len(self.data) == 0:
            return None

        self.swap(0, len(self.data)-1)
        val = self.data.pop()
        self.bubbleDown()
        return val

    def swap(self, i1, i2):
        temp = self.data[i2]
        self.data[i2] = self.data[i1]
        self.data[i1] = temp

    def bubbleDown(self, currentIndex=0):
        leftChild = (currentIndex * 2) + 1
        rightChild = leftChild + 1
        if (leftChild >= len(self.data)):
            return
        elif (rightChild >= len(self.data)):
            if self.data[leftChild] > self.data[currentIndex]:
                self.swap(leftChild, currentIndex)
                # return self.bubbleDown(leftChild)
            else:
                return
        else:
            biggerChild = leftChild if (
                self.data[leftChild] > self.data[rightChild]) else rightChild
            if self.data[biggerChild] > self.data[currentIndex]:
                self.swap(biggerChild, currentIndex)
                return self.bubbleDown(biggerChild)
            else:
                return

    def bubbleUp(self, currentIndex):
        if currentIndex == 0: return
        parent = (currentIndex-1)//2
        if self.data[parent] < self.data[currentIndex]:
            self.swap(parent, currentIndex)
            return self.bubbleUp(parent)


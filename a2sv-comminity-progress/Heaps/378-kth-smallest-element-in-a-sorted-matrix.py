class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        smallest = matrix[0][0]
        n = len(matrix[0])
        heap = MinHeap((n*n)+1-k)
        for i in matrix:
            for j in i:
                heap.add(j)
        return heap.data[0]


        


class MinHeap:
    def __init__(self, maxVal):
        self.maxLength = maxVal
        self.data = []
    
    def add(self, val):
        if len(self.data) == 0: 
            self.data = [val]
            return
        if (len(self.data) < self.maxLength):
            self.data.append(val)
            return self.bubbleUp(len(self.data)-1)
        if len(self.data) == self.maxLength:
            if val < self.data[0]:
                return
            else:
                self.data[0] = val
                self.bubbleDown()

        # if (len(self.data)) > self.maxLength:
        #     self.removeBiggestLeaf()
    
    def bubbleDown(self, index = 0):
        if index >= len(self.data): return
        leftChild = index * 2 + 1
        rightChild = leftChild + 1
        if leftChild >= len(self.data):
            return
        elif rightChild >= len(self.data):
            if self.data[leftChild] < self.data[index]:
                self.data[leftChild], self.data[index] = self.data[index], self.data[leftChild] 
            return
        else:
            smallerChild = rightChild if self.data[rightChild] < self.data[leftChild] else leftChild
            if self.data[smallerChild] < self.data[index]:
                self.data[smallerChild], self.data[index] = self.data[index], self.data[smallerChild] 
                return self.bubbleDown(smallerChild)


            


    
    def bubbleUp(self, index):
        if index == 0: return
        parentIndex = (index-1)//2
        if self.data[parentIndex] > self.data[index]:
            self.data[parentIndex], self.data[index] = self.data[index], self.data[parentIndex]
            return self.bubbleUp(parentIndex)
    
    def removeBiggestLeaf(self):
        leftMostLeaf = (len(self.data)+1)/2
        leaves = self.data[leftMostLeaf:]
        biggestLeafIndex = 0
        for i in range(len(leaves)):
            if leaves[i] > leaves[biggestLeafIndex]:
                biggestLeafIndex = i
        self.data[leftMostLeaf + biggestLeafIndex], self.data[-1] = self.data[-1], self.data[leftMostLeaf + biggestLeafIndex]
        # self.bubbleUp(leftMostLeaf + biggestLeafIndex)
        # self.data.pop()




matrix = [[1,5,9],[10,11,13],[12,13,15]]; k = 8
print(Solution().kthSmallest(matrix, k))
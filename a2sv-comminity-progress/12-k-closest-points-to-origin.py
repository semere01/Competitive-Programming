class Sorter:
    def quickSort(self, arr):
        self.arr = arr
        self.qs(0, len(arr) - 1)
        return self.arr
    
    def qs(self, left, right):
        if left >= right: return

        pivot = self.arr[((right+left)// 2)][2]
        index = self.partition(pivot, left, right)
        self.qs(left, index-1)
        self.qs(index, right)

    
    def partition(self, pivot, left, right):
        while left <= right:
            while self.arr[left][2] < pivot: left += 1
            while self.arr[right][2] > pivot: right -= 1

            if (left <= right):
                (self.arr[left], self.arr[right]) = (self.arr[right], self.arr[left])
                left +=1
                right -=1
        
        return left

class Solution:
    def calculateDistance(self, x1, y1):
        xSq = (x1)
        ySq = (y1)
        ans = ((xSq ** 2) + (ySq ** 2)) ** (1/2)
        return ans
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:        
        distancesSorted = Sorter().quickSort([[x1[0], x1[1],self.calculateDistance(x1[0], x1[1])] for x1 in points].copy())
        return([[x,y] for [x,y,d] in distancesSorted[:k]])






class Sorter:
    def quickSort(self, arr):
        self.arr = arr
        self.qs(0, len(arr) - 1)
        return self.arr
    
    def qs(self, left, right):
        if left >= right: return

        pivot = self.arr[((right+left)// 2)][0]
        index = self.partition(pivot, left, right)
        self.qs(left, index-1)
        self.qs(index, right)

    
    def partition(self, pivot, left, right):
        while left <= right:
            while self.arr[left][0] < pivot: left += 1
            while self.arr[right][0] > pivot: right -= 1

            if (left <= right):
                (self.arr[left], self.arr[right]) = (self.arr[right], self.arr[left])
                left +=1
                right -=1
        
        return left

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        i = 0
        Sorter().quickSort(intervals)
        while i < (len(intervals)-1):
            currentElement = intervals[i]
            nextElement = intervals[i+1]
            if currentElement[1] >= nextElement[0]:
                intervals[i] = [min(currentElement[0], nextElement[0]), max(currentElement[1], nextElement[1])]
                intervals.pop(i+1)
            else:
                i+=1
        return intervals


# question [[1,4],[0,0]] 
# output [[0,4]]
# expected [[0,0],[1,4]]



print(Solution().merge([[1,4],[0,0]]))

        
class Sorter:
    def quickSort(self, arr):
        self.arr = arr
        self.qs(0, len(arr) - 1)
        return self.arr
    
    def qs(self, left, right):
        if left >= right: return

        pivot = self.arr[((right+left)// 2)]
        index = self.partition(pivot, left, right)
        self.qs(left, index-1)
        self.qs(index, right)

    
    def partition(self, pivot, left, right):
        while left <= right:
            while (str(pivot) + str(self.arr[left]) < (str(self.arr[left]) + str(pivot))): left += 1
            while (str(pivot) + str(self.arr[right]) > (str(self.arr[right]) + str(pivot))): right -= 1
            if (left <= right):
                (self.arr[left], self.arr[right]) = (self.arr[right], self.arr[left])
                left +=1
                right -=1
        
        return left

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        ans = (''.join([str(x) for x in Sorter().quickSort(nums)])).lstrip()
        if (int(ans)): return ans
        return '0'
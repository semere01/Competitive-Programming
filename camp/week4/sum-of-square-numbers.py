class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = [i*i for i in range(0,int(c**0.5)+1)]
        for num in squares:
            if self.bs(squares,0,len(squares)-1,c-num):
                return True
        return False
    
    def bs(self,squares,low,high,target):
        if low<=high:
            mid = (low+high)//2
            if squares[mid] == target:
                return True
            if squares[mid] > target:
                return self.bs(squares,low,mid-1,target)
            return self.bs(squares,mid+1,high,target)
        return False
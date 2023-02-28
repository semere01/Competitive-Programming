class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n < 0):
            return 1/(self.myPow(x,-1*n))
        elif (n == 0):
            return 1
        elif (n==1):
            return x
        elif (n%2 == 1):
            return self.myPow(x, n//2) * self.myPow(x, (n//2)+ 1)
        else:
            x = self.myPow(x, n//2)
            return x * x


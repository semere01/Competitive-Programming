class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = []
        for i in range(n+1):
            if i == 0:
                arr.append(0)
            elif i == 1:
                arr.append(1)
            elif not (i % 2): # even
                arr.append(arr[i//2])
            else: # odd
                arr.append(arr[i//2] + arr[(i//2)+1])
        
        return max(arr)
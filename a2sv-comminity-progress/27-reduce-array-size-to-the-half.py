class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        dp = {}
        
        for i in arr:
            dp[i] = 1 + dp.get(i, 0)

        dp = {k:v for k,v in sorted(dp.items(), key=lambda x: x[1], reverse=True)}
        
        elements_to_remove = 0
        n = len(arr)
        
        for i in dp:

            n -= dp[i]
            elements_to_remove += 1
            if n <= len(arr)//2:
                return elements_to_remove






'''
# My first implementation
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        initialSize = len(arr)
        arr = sorted(arr, key=lambda x:arr.count(x), reverse=True)
        sizeDec = 0
        counter = 0
        while (sizeDec*2 < initialSize):
            sizeDec += arr.count(arr[sizeDec])
            counter += 1
        return counter
'''


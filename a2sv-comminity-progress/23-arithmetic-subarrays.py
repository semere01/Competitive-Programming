class Solution:
    def checkArithmetic(self, nums: list[int], l: int, r: int) -> bool:
        if (l >= r): return False
        nums = sorted(nums[l:r+1]) # O(n log(n))
        originalDiff = nums[1] - nums[0]
        for i in range(0, r-l): # O(n)
            if nums[i+1] - nums[i] != originalDiff: return False     
        return True
    
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        finalList = []
        for i in range(len(l)):
            finalList.append(self.checkArithmetic(nums, l[i], r[i]))
        return finalList

ls = [0,1,6,4,8,7]
rs = [4,4,9,7,9,10]

for i in range(len(ls)): print(Solution().checkArithmetic([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], ls[i], rs[i]))

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        uniqueOnes = set()
        for i in range(len(nums)):
            num = nums[i]
            uniqueOnes.add(num)
            num = list(str(num))
            for i in range(len(num)//2):
                num[i], num[len(num)-1-i] = num[len(num)-1-i], num[i]
            uniqueOnes.add(int("".join(num)))
            
        return len(uniqueOnes)
            
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        f = set()  
        for  i in range(len(nums)):
           
    
            d = 2

            while d * d <= nums[i]:
                while nums[i] % d == 0:
                    f.add(d)
                    nums[i] //= d
                d += 1
            if nums[i] > 1:
                f.add(nums[i])

        return len(f)
                  

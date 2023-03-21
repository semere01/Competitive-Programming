class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # Initialize Variables
        n = len(nums)
        nice_array_count = 0
        p0 = 0
        p1 = 0
        current_count = 0
        
        # Slide through our list
        while p1 < n:
            if nums[p1] % 2:
                current_count += 1
            if current_count == k:
                nice_array_count += 1
                while nums[p0] %2 == 0:
                    p0 += 1
                p0 += 1
                current_count -= 1
            
            p1 +=1
        
        return nice_array_count

print(Solution().numberOfSubarrays([1,1,2,1,1], 3))

            


            







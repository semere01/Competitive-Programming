

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        f = None
        s = None
        for num in nums:
            if (f == None or num <= f  ):
                f = num
            elif ( s == None or num <= s ):
                s = num
            else:
                return True
        
        return False
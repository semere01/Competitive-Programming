class Solution:

    def PredictTheWinner(self, nums: list[int]) -> bool:
        self.nums = nums
        self.switch = 1
        max1 = self.playP1(0,0,0,len(nums)-1)
        self.switch = 2
        max2 = self.playP1(0,0,0,len(nums)-1)
        return max1 >= max2
    

    def playP1(self,  p1Score, p2Score, left, right):
        nums = self.nums
        if (left > right or right < 0 or left >= len(nums)):
            if (self.switch == 1):
                return p1Score
            else:
                return p2Score
            return p1Score < p2Score
        else:
            v1 = self.playP2( p1Score+nums[left],p2Score, left+1, right )
            v2 = self.playP2(p1Score+nums[right], p2Score, left, right-1)
            return  max(v1 , v2 )
    
    def playP2(self,  p1Score, p2Score, left, right):
        nums = self.nums
        if (left > right or right < 0 or left >= len(nums)):
            if (self.switch == 1):
                return p1Score
            else:
                return p2Score
        else:
            v1 = self.playP1(p1Score, p2Score+nums[left], left+1, right)
            v2 = self.playP1(p1Score, p2Score+nums[right], left, right-1)
            return  max(v1 , v2 )


    

    
# print(Solution().PredictTheWinner([1,5,233,7]))
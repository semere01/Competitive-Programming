class Solution:

    def PredictTheWinner(self, nums: list[int]) -> bool:
        self.p0 = 0
        self.p1 = 0
        self.nums = nums
        self.updateScores(0,0, len(nums))
        return self.p0 >= self.p1
    
    def updateScores(self, player: int, init:int, final: int):
        score = 0
        print(f"init({init}) - final({final})")
        if (final-init) == 0:
            return
        if self.nums[init] > self.nums[final-1]:
            score = self.nums[init]
            init += 1
        else:
            score = self.nums[final-1]
            final -= 1
        
        if (player == 0):
            player = 1
            print(f"added {score} to p0, so from {self.p0} to {self.p0 + score}")
            self.p0 += score
        elif (player == 1):
            player = 0
            print(f"added {score} to p1, so from {self.p1} to {self.p1 + score}")
            self.p1 += score
        
        self.updateScores(player, init, final)


print(Solution().PredictTheWinner([1,5, 233,7]))
        


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        numsLength = len(nums)
        k = k % numsLength
        numsCopy = [None] * numsLength
        for i in range(numsLength):
            numsCopy[i] = nums[i-k]

            
        # numsCopy = nums[k+1:] + nums[:k+1]
        for i in range(numsLength):
            nums[i] = numsCopy[i]


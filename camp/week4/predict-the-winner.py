class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(numbers,start,end,turn):
            if start==end:
                return turn*nums[start]
            a=turn*nums[start]+winner(numbers,start+1,end,-turn)
            b=turn*nums[end]+winner(numbers,start,end-1,-turn)
            return turn*max(turn*a,turn*b)

        return winner(nums,0,len(nums)-1,1)>=0

       

        
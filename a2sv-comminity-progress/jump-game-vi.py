import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp=[float('-inf')]*(len(nums))
        dp[-1]=nums[-1]
        heap=[-1*nums[-1]]
        heapq.heapify(heap)
        queue=defaultdict(lambda :0)
        queue[nums[-1]]+=1
        for i in range(len(nums)-2,max(-1,len(nums)-k-1),-1):
            dp[i]=(-1*heap[0])+nums[i]
            heapq.heappush(heap,-1*dp[i])
            queue[dp[i]]+=1
        for i in range(len(nums)-k-1,-1,-1):
            while(len(heap)>0 and queue[-1*heap[0]]==0):
                  heapq.heappop(heap)
            dp[i]=(-1*heap[0])+nums[i]
            queue[dp[i]]+=1
            heapq.heappush(heap,-1*dp[i])
            queue[dp[i+k]]=max(queue[dp[i+k]]-1,0)
   
        return dp[0]
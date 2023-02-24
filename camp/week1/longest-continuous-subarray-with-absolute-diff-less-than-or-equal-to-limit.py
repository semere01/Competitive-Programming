from collections import deque
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        monoQ = deque()
        l_pointer = 0
        r_pointer = 0
        biggestList = 0
        currentCount = 0

        # print(Solution().longestSubarray([2,2,2,4,4,2,5,5,5,5,5,2], 2))
        while (r_pointer < len(nums)):
            if (len(monoQ) == 0 or nums[monoQ[-1]] <= nums[r_pointer]):
                monoQ.append(r_pointer)
            elif nums[monoQ[0]] >= nums[r_pointer]:
                monoQ.appendleft(r_pointer)
            if abs(nums[monoQ[-1]] - nums[monoQ[0]]) <= limit:
                pass
            else:
                if (r_pointer - l_pointer ) > biggestList:
                    biggestList = r_pointer - l_pointer 
                # l_pointer = min(monoQ[0], monoQ[-1])
                if monoQ[0] < monoQ[-1]:
                    l_pointer = monoQ[0] + 1
                    monoQ.popleft()
                else:
                    l_pointer = monoQ[-1] + 1
                    monoQ.pop()
            r_pointer += 1
            while (len(monoQ) > 0 and monoQ[-1] < l_pointer):
                monoQ.pop()
            while (len(monoQ) > 0 and monoQ[0] < l_pointer):
                monoQ.popleft()


        if (r_pointer - l_pointer ) > biggestList:
            biggestList = r_pointer - l_pointer 

        
        return biggestList


print(Solution().longestSubarray([8,2,4,7], 4))
print(Solution().longestSubarray([10,1,2,4,7,2], 5))
print(Solution().longestSubarray([4,2,2,2,4,4,2,2], 0))
# print(Solution().longestSubarray([2,2,2,4,4,2,5,5,5,5,5,2], 2))

                
                
            
            
            



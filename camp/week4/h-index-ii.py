class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if (citations[-1] == 0): return 0
        if (len(citations) <= citations[0]):
            return len(citations)
        
        left = -1
        h_index = -1
        right = len(citations)
        while (left + 1 < right ):
            mid = (left + right) // 2
            mid_val = citations[mid]
            num_of_rem = len(citations) - mid - 1
            if (num_of_rem >= mid_val):
                h_index = num_of_rem
                left = mid
            else:
                right = mid
                
        return h_index
            
print(Solution().hIndex([1,1]))




        # return 1
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(k):
            count = 0
            start = 0
            stack , dict_ = [] , {}
            odd_freq = 0
            for i in range(0 , len(nums)):
                stack.append(nums[i])
                 
                if nums[i] % 2 == 1:
                    odd_freq += 1

                if odd_freq <= k:
                    count += (i - start + 1)

                elif odd_freq > k: 
                    while len(stack) != 0 and odd_freq > k:
                        pop = stack.pop(0)
                        
                        if pop % 2 == 1:
                            odd_freq -= 1
                       
                        start += 1  
                        if odd_freq <= k:
                            count += (i - start + 1)
            return count                

        return helper(k) - helper(k - 1)    
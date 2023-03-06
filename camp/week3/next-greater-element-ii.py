class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack  = []
      
        num = nums + nums
        for i in range(len(nums) ):
            inc = 0
            for j in range(i,len(num)):
                if nums[i] < num[j]:
                    inc+=1
                    stack.append(num[j])
                    break
            if inc == 0:
                stack.append(-1)
        return stack
            
        
        
       
            
            
            
             
        
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        finalList = []
        for i in range(len(nums1)):
            n = nums1[i]
            ind = nums2.index(n)
            for j in range(ind+1, len(nums2)):
                if nums2[j] > n:
                    finalList.append(nums2[j])
                    break
            if len(finalList) < i+1: finalList.append(-1)
        
        return finalList

tests = [
   ([4,1,2], [1,3,4,2]), 
   ([2,4], [1,2,3,4]), 
]
for test in tests: print(Solution().nextGreaterElement(test[0], test[1]))
        
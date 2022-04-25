class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        def findMaxFreq(nums: list, num: int, bank: int):
            firstIndex = nums.index(num)
            converts = 0
            if (firstIndex == 0): return 0;
            while (firstIndex != 0 and bank > 0):
                countOfSmaller = firstIndex - nums.index(nums[firstIndex-1])
                firstIndex = nums.index(nums[firstIndex-1])
                costOfEach = num - nums[firstIndex]
                currentIncrease = bank // costOfEach
                converts = converts + (currentIncrease if currentIncrease <= countOfSmaller else countOfSmaller)
                bank -= costOfEach * converts
            return (converts)
        maxFreq = nums.count(nums[0])
        tests = [maxFreq]
        counts = [maxFreq]
        for i in range(1, len(nums)):
            counts.append(nums.count(nums[i]))
            currentFreq = findMaxFreq(nums, nums[i], k) + nums.count(nums[i])
            tests.append(currentFreq) 
            maxFreq = currentFreq if currentFreq > maxFreq else maxFreq 
        # print("counts, ", counts)
        print("counts,   ", end = '')
        for c in counts: print(f"{c}   ", end='')
        print()
        print("tests,  ", tests)
        return maxFreq

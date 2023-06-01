class Solution:
    def __init__(self):
        self.cache = {}

    def max(self, index: int, first: bool) -> int:
        if index in self.cache:
            return self.cache[index]
        if index >= len(self.nums):
            return 0
        if index == len(self.nums) - 1:
            if first:
                return 0
            else:
                return self.nums[index]
        if index == len(self.nums) - 2:
            if first:
                return self.nums[index]
            else:
                return max(self.nums[index:])
        self.cache[index] = max(
            self.nums[index] + self.max(index + 2, first), self.max(index + 1, first)
        )
        return self.cache[index]
        pass

    def rob(self, nums: list[int]) -> int:
        self.nums = nums
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        for i in range(len(nums) - 1, -1, -1):
            self.max(i, True)

        max_1 = self.max(0)
        self.cache = {}
        for i in range(len(nums) - 1, -1, -1):
            self.max(i, False)
        max_2 = self.max(0)
        return max(max_1, max_2)

        if len(nums) % 2:  # is odd
            max_2 = self.max(1)
            self.cache = {}
            nums.pop()
            self.nums = nums
            for i in range(len(nums) - 1, -1, -1):
                self.max(i)
            max_1 = self.max(0)
            return max(max_1, max_2)
        else:  # is even
            return max(self.max(0), self.max(1))

        pass

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        last = len(names)
        while (last > 0):
            for i in range(0, len(names)-1):
                if heights[i] < heights[i+1]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    names[i], names[i+1] = names[i+1], names[i]
            last -= 1
        return names


print(Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))

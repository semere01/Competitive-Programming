class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 != 0:
            return []
        x = (num-3)//3
        return [x, x+1, x+2]
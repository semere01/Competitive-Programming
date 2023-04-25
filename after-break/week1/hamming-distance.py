class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bits = 0
        mask = x ^ y
        while mask != 0:
            mask = mask & (mask - 1)
            bits += 1
        return bits
        
class Solution:

    def op_remaining(self, idx: int, rem: int, coins: list[int], cache):
        if (idx, rem) in cache:
            return cache[(idx, rem)]
        if rem == 0:
            return 0
        if rem < 0 or idx >= len(coins):
            return float("inf")

        cache[(idx, coins)]= min(
            1 + self.op_remaining(idx, rem - coins[idx], coins, cache),
            self.op_remaining(idx + 1, rem, coins, cache),
        )
        return cache[(idx, rem)]

    def coinChange(self, coins: list[int], amount: int) -> int:
        ans = self.op_remaining(0, amount, coins, {})
        if ans == float("inf"):
            return -1
        return ans
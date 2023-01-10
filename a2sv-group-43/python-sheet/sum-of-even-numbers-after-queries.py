class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        totals = []
        total = sum([i for i in nums if not i % 2])
        for query_index in range(len(queries)):
            value = queries[query_index][0]
            index = queries[query_index][1]

            old_nums_at_index = nums[index]
            nums[index] = nums[index] + value

            if not old_nums_at_index % 2:
                total -= old_nums_at_index
            if not nums[index] % 2:
                total += nums[index]

            totals.append(total)

        return totals

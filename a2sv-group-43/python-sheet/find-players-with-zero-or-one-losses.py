from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winners = [match[0] for match in matches]
        one_time_losers = []

        loss_counts = defaultdict(int)
        for match in matches:
            loss_counts[match[1]] += 1

        index = 0
        # for index in range(len(winners)):
        while (index < len(winners)):
            if loss_counts[winners[index]] != 0:
                winners.pop(index)
            else:
                index += 1
        for key in loss_counts.keys():
            loss_count = loss_counts[key]
            if (loss_count) == 1:
                one_time_losers.append(key)
        winners = sorted(list(set(winners)))
        one_time_losers = sorted(list(set(one_time_losers)))
        
        return [winners, one_time_losers]

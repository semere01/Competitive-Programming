from collections import Counter


class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        validScores = []
        for i in range(22):
            validScores.append(2**i)

        counter = Counter(deliciousness)
        final = 0
        keys = list(counter.keys())

        for i in range(len(keys)):
            d = keys[i]
            for vs in validScores:
                count = counter[vs-d]
                if (count):
                    print("count yes")
                    if (vs-d) == d:
                        final += (count*(count-1))//2
                    else:
                        final += (counter[vs-d] * counter[d])
            counter[d] = 0

        return (final % ((10**9) + (7)))

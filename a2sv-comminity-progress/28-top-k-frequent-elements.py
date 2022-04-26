from collections import Counter
class Solution:
    def topKFrequent(self, lst: list[int], k: int) -> list[int]:
        lst = [n for n,count in Counter(lst).most_common() for i in range(count)]
        counter = 0
        finalList = []
        pointer = 0
        while (counter < k):
            print("pointer: ", pointer)
            counter += 1
            finalList.append(lst[pointer])
            pointer += lst.count(lst[pointer])
        return finalList 
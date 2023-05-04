import heapq


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        countMap = {}
        for word in words:
            currentCount = countMap.get(word, 0)
            countMap[word] = currentCount + 1
        
        
        countList = []
        wordList = []

        for word in countMap.keys():
            wordList.append(word)
            countList.append(countMap[word])
        
        heap = []
            
        for index in range(len(countList)):
            count = countList[index]
            word = wordList[index]
            heapq.heappush(heap, (-1 *count, word))
            # if len(heap) > k:
            #     heapq.heappop(heap)
        
        returnData = []
        for i in range(k):
            d = heapq.heappop(heap)
            
            returnData.append(d[1])
            
        
        return returnData

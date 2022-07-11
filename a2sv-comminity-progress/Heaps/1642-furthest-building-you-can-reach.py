import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        heap = []
        for i in range(N-1):
            h = heights[i+1] - heights[i]
            if h<=0: continue
            heapq.heappush(heap, h)
            if len(heap) > ladders:
                min_h = heapq.heappop(heap)
                bricks -= min_h
            if bricks < 0:
                return i
        return N-1
















        # for i in range(1, len(heights)):
        #     if heights[i] - heights[i-1] > 0:
        #         heightMap.append(heights[i] - heights[i-1])
        #     else:
        #         heightMap.append(0)
        # numberOfJumps = 0
        # for b in range(1,len(heights)):
        #     currentHeightDiff = heights[b] - heights[b-1]
        #     if (currentHeightDiff > 0):
        #         heightMap.append(currentHeightDiff)
        #     else:
        #         heightMap.append(0)

        #     heap = MaxHeap(heightMap)
        #     availableLadders = ladders

        #     while availableLadders:
        #         if heap.isEmpty():
        #             break
        #         if heap.pop():
        #             availableLadders -= 1
        #     if heap.isEmpty() or (bricks >= sum(heap.data)):
        #         numberOfJumps += 1
        #     else:
        #         break
        # return numberOfJumps
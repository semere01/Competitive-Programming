class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        if (arr == sorted(arr)): return []
        flips = []
        def flip(arr, k): # k is 1 indexed
            flips.append(k)
            return ([arr[i] for i in range(k-1, -1, -1)] + arr[k:])
        counter = 0
        while counter < len(arr):
            largestIndex = 0
            for i in range(0, len(arr) - counter):
                if arr[i] > arr[largestIndex]: largestIndex = i
            arr = flip(arr, largestIndex + 1)
            arr = flip(arr, len(arr) - counter)
            counter += 1
        return (flips)
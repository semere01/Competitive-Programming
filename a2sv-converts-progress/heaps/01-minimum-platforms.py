class Solution:
    def minimumPlatform(self, n, arr, dep):
        if n == 0: return 0
        arr.sort()
        dep.sort()

        i, j, tracks, result = [0, 0, 0, 0]
        while (i < n and j < n):
            if arr[i] <= dep[j]:
                i += 1
                tracks += 1
            else:
                j += 1
                tracks -= 1
            if tracks > result:
                result = tracks

        return result

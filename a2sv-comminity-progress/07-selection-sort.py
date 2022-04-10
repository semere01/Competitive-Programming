class Solution: 
    def select(self, arr, i):
        for j in range(i, n):
            if arr[j] < arr [i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        return arr


    
    def selectionSort(self, arr,n):
        minIndex = 0;
        for i in range(n-1):
            minIndex = i
            self.select(arr, i)
        
        return arr;


if __name__ == "__main__":
    arr = [5,3,5,2,6,34,7,2]
    n = len(arr)
    s = Solution()
    print(s.selectionSort(arr, n))
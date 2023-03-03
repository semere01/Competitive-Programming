class Solution: 
    def select(arr, i):
        return i

    def selectionSort(self, arr: list,n: int):
        for current_index in range(len(arr)):
            current_index_copy = current_index
            for j in range(current_index, len(arr)):
                if arr[current_index_copy] > arr[j]:
                    current_index_copy = j
            arr[current_index], arr[current_index_copy] = arr[current_index_copy], arr[current_index]
    
        return arr


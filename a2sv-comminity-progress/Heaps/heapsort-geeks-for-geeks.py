
class Solution:
    #Heapify function to maintain heap property.                                      [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
    def heapifyDown(self,heap, n, i):
        n = len(heap)
        while(i < n):
            leftIndex = 2*i + 1
            rightIndex = 2*i + 2
            if (leftIndex) >= n: 
                return
            elif (rightIndex) >= n:
                if heap[leftIndex] > heap[i]:
                    temp = heap[leftIndex]
                    heap[leftIndex] = heap[i]
                    heap[i] = temp
                return
            else:
                if heap[leftIndex] > heap[rightIndex]: 
                    indexToSwap = leftIndex
                else:
                    indexToSwap = rightIndex
                if heap[i] < heap[indexToSwap]:
                    temp = heap[indexToSwap]
                    heap[indexToSwap] = heap[i]
                    heap[i] = temp
                i = indexToSwap

    def heapifyUp(self,heap, n, i):
        while(i != 0):
            parentIndex = (i - 1) // 2
            if (heap[i] > heap[parentIndex] ):
                temp = heap[i]
                heap[i] = heap[parentIndex]
                heap[parentIndex] = temp
                i = parentIndex
            else: break
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        heap = []
        for value in arr:
            self.addToHeap(heap, value)
        for i in range(n):
            arr[i] = heap[i]
    
    def addToHeap(self, heap, i):
        heap.append(i)
        self.heapifyUp(heap, len(heap), len(heap)-1)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, len(arr))
        sortedArr = []
        while (len(arr)):
            sortedArr.insert(0, arr[0])
            arr[0] = arr[-1]
            arr.pop()
            self.heapifyDown(arr, len(arr), 0)
        for i in range(len(sortedArr)):
            arr.append(sortedArr[i])

        #code here

s = Solution()
t = [int(s) for s in "932 66 777 426 127 404 63 281 426 317 735 628 543 78 31 811 626 104 389 412 687 296 35 252 441 675 604 770 342 284 917 274 702 46 53 829 450 116 463 229 786 198 857 329 276 888 140 254 992 530 18 31 178 405 284 619 80 240 742 423 876 659 49 931 57 102 760 859 571 575 88 357 773 945 38 401 186 531 655 530 413 673 562 591 79 198 563 159 790 305 582 666 316 984 597 373 86 710 584 9 285 673 718 411 970 757 812 508 288 468 39 701 493 953 644 924 151 559 84 293 864 18 959 532 2 909 257 441 619 842 802 256 515 521 667 837 630 832 346 918 652 385 971 145 690 967".split(" ")]
s.HeapSort(t, len(t))


        


    
    #Function to sort an array using Heap Sort.    
    # def HeapSort(self, arr, n):
        #code here

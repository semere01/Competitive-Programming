

import heap


def heapSort(data: list[int]) -> list[int]:
    myHeap = heap.heapClass()
    sortedArray = []
    for datum in data:
        myHeap.addToHeap(datum)
    for datum in data:
        sortedArray.append(myHeap.getMin())
    return sortedArray


testData = [4,3,2,5,7,43,1,7,4,2,3,6,9,5,3,1]
# heapSort(testData)
# print(heapSort(testData))
assert(sorted(testData) == heapSort(testData))
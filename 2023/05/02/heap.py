from heapq import heappush


class heapClass:
    def __init__(self):
        self.data = []
        pass

    def addToHeap(self, n):
        self.data.append(n)
        current_index = len(self.data) - 1
        parent_index = self.getParentIndex(current_index)
        while (parent_index != -1 and self.data[parent_index] > n):
            self.data[parent_index], self.data[current_index] = self.data[current_index], self.data[parent_index]
        pass

    def getParentIndex(self, n):
        if (n == 0):
            return -1
        else:
            return ((n-1) // 2)

    def getMin(self):
        if len(self.data) == 0:
            return -1
        last_index = len(self.data) - 1
        self.data[0], self.data[last_index] = self.data[last_index], self.data[0]
        return_data = self.data.pop()
        self.heapifyDown()
        return return_data

    def heapifyDown(self):
        current_index = 0
        while self.getSmallerChildIndex(current_index) != -1:
            smaller_child_index = self.getSmallerChildIndex(current_index)
            if (self.data[smaller_child_index] < self.data[current_index]):
                self.data[current_index], self.data[smaller_child_index] = self.data[smaller_child_index], self.data[current_index]
                current_index = smaller_child_index
            else:
                break

    def getLeftChildIndex(self, n):
        return (n*2) + 1

    def getRightChildIndex(self, n):
        return (n*2) + 2

    def getSmallerChildIndex(self, n):
        left_child = (n*2) + 1
        right_child = (n*2) + 2

        if (right_child >= len(self.data) and left_child >= len(self.data)):
            return -1

        if (right_child >= len(self.data)):
            return left_child

        if (self.data[left_child] > self.data[right_child]):
            return right_child

        return left_child

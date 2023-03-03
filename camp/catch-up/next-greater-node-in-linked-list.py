# Definition for singly-linked list.

class uniqueStack:
    def __init__(self):
        self.data = []
    def pop(self):
        if self.data == []: return None
        return self.data.pop()
    def peek(self):
        if self.data == []: return None
        return self.data[-1]
    def push(self, newValue):
        self.data = self.data + [newValue]
    def isEmpty(self):
        return len(self.data)==0
    def isNotEmpty(self):
        return not self.isEmpty()
    def getAll(self):
        return self.data

class Solution:
    def reverseList(self, head):
        next = head
        prev = head.next
        head.next = None
        while prev:
            temp = prev.next
            prev.next = next
            next = prev
            prev = temp
        return next

    # def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    def nextLargerNodes(self, head):
        if not head: return
        if not head.next: return [0]
        stack = uniqueStack()
        finalList = [0]
        current = self.reverseList(head)
        stack.push(current.val)
        while (current.next):
            current = current.next
            if current.val == stack.peek():
                finalList = [finalList[0]] + finalList
            if current.val < stack.peek():
                finalList = [stack.peek()] + finalList
                stack.push(current.val)
            if current.val > stack.peek():
                while stack.isNotEmpty() and stack.peek() <= current.val:
                    stack.pop()
                if stack.isEmpty():
                    finalList = [0] + finalList
                    stack.push(current.val)
                else:
                    finalList = [stack.peek()] + finalList
                    stack.push(current.val)
        return finalList
            
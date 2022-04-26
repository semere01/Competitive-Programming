class Solution:
    def isValid(self, s: str) -> bool:
        stack = [];
        opening = ["[", "(", "{"]
        closing = ["]", ")", "}"]
        for i in s:
            if i in opening: stack.append(i)
            if i in closing:
                if not stack: return False
                if (stack[-1] not in opening): return False
                if closing[opening.index(stack[-1])] != i: return False 
                stack.pop() 
        if len(stack): return False
        return True
       
# print(Solution().isValid("()"))

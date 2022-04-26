class Solution:
    def evalRPN(self, tokens: list[str]) -> int: 
        myStack = []
        operators = ["+", "-", "/", "*"]
        for token in tokens:
            if token in operators:
                # handle operand
                operand1 = myStack.pop()
                operand2 = myStack.pop()
                myStack.append(str(int(eval(operand2 + token + operand1))))
            else:
                # handle number
                myStack.append(token)
        return myStack[0]



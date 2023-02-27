class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        nums = [int(tokens[0]), int(tokens[1])]
        for i in range(2, len(tokens)):
            if tokens[i].isdigit() or len(tokens[i])>1:
                nums.append(int(tokens[i]))
            else:
                a, b = nums[-2], nums[-1]
                if tokens[i] == '+':
                    nums = nums[:-2] + [a + b]
                elif tokens[i] == '-':
                    nums = nums[:-2] + [a - b]
                elif tokens[i] == '*':
                    nums = nums[:-2] + [a * b]
                elif tokens[i] == '/':
                    nums = nums[:-2] + [int(a / b)]
        return nums[-1]

        
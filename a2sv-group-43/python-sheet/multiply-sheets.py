from random import randint


class Solution:
    def multiplyBySingle(self, num1: str, num2: str) -> str:
        bucket = "0"
        total = ""
        p = len(num1) - 1
        while p >= 0:
            curr = str((int(num1[p]) * int(num2)) + int(bucket))
            if (len(curr) == 2):
                total = curr[-1] + total
                bucket = curr[0]
            else:
                total = curr + total
                bucket = "0"
            p -= 1
        if (bucket != "0"):
            total = bucket + total
        return total

    def multiply(self, num1: str, num2: str) -> str:
        matrix = []
        largestLength = 0
        p = len(num2)-1
        while p >= 0:
            v1 = self.multiplyBySingle(num1, num2[p])
            v2 = ("0" * (len(num2)-p-1))
            curr = v1 + v2
            if (largestLength < len(curr)):
                largestLength = len(curr)
            matrix.append(curr)
            p -= 1

        p = largestLength - 1
        holder = 0
        final = ""
        while p >= 0:
            curr = str(sum(int((s.rjust(largestLength, '0'))
                       [p]) for s in matrix) + holder)
            if (len(curr) == 1):
                final = curr + final
                holder = 0
            else:
                final = curr[-1] + final
                holder = int(curr[:len(curr)-1])
            p -= 1
        if (holder):
            final = str(holder) + final

        zeroCount = 0
        while (zeroCount < len(final) and final[zeroCount] == "0"):
            zeroCount += 1
        if (zeroCount == len(final)):
            return "0"
        else:
            return final[zeroCount:]

        # return final


# print(Solution().multiply("98", "95"))
# print(98*95)

for i in range(100):
    lower = 1
    higher = 435
    n1 = randint(lower, higher)
    n2 = randint(lower, higher)
    print(
        f"test case {i} with {n1} and {n2} - {str(n1*n2)==Solution().multiply(str(n1), str(n2))}")

class Solution:
    def isCharacter(self, s) -> bool:
        num = ord(s)
        if ((num >= ord("a")) and (num <= ord("z"))):
            return True
        if ((num >= ord("A")) and (num <= ord("Z"))):
            return True
        if ((num >= ord("0")) and (num <= ord("9"))):
            return True
        return False

    def isEquivalent(self, x, y) -> bool:
        x = ord(x)
        y = ord(y)
        diff = ord("a")-ord("A")
        if (x == y):
            return True
        if (x >= ord("a") and x <= ord("z")):
            if (y+diff == x):
                return True
        if (x >= ord("A") and x <= ord("Z")):
            if (x+diff == y):
                return True
        return False

    def iseq(self, x, y) -> bool:
        print(f"testing if {x} and {y} are eq - {self.isEquivalent(x,y)}")
        return self.isEquivalent(x, y)

    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        l = len(s)
        i = 0
        j = l-1
        while (i < l and j >= 0):
            print('iterate')
            while (i < l and not self.isCharacter(s[i])):
                i += 1
            while (j >= 0 and not self.isCharacter(s[j])):
                j -= 1
            if (i < l and j >= 0 and not self.isEquivalent(s[i], s[j])):
                return False
            i += 1
            j -= 1

        return True


tests = [
    # ".,",
    "0P",
    # "A man, a plan, a canal: Panama",
]

for test in tests:
    print(f"{test} - {Solution().isPalindrome(test)}")

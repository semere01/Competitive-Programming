class Solution:
    def isPalindrome(self, s: str) -> str:
        return s==s[len(s)::-1]

    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) == 1: return ""

        for i in range(len(palindrome)):
            if palindrome[i] != "a":
                temp = palindrome[i]
                palindrome[i] = "a"
                if (isPalindrome(''.join(palindrome))):
                    palindrome[i] = temp
                    palindrome[-1] = "b"
                return ''.join(palindrome)
        palindrome[-1] = "b"
        return ''.join(palindrome)



tests = [
"abccba",
"a",

]
        
for t in tests: print(Solution().breakPalindrome(t))


        
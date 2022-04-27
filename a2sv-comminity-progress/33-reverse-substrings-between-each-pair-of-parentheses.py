class Solution:
    def reverseParentheses(self, s: str) -> str:
        z=[]
        for i,j in enumerate(s):
            if j=="(":
                z.append(i)
            elif j==")":
                s=s[:z[-1]]+s[z[-1]:i][::-1]+s[i:]
                z.pop()
        s=s.replace("(","")
        s=s.replace(")","")
        return s
                

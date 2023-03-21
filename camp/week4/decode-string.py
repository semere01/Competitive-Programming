# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

class Solution:
    def decodeString(self, s: str) -> str:
        p = 0
        s = list(s)
        ans = self.dd(p, s)
        return ''.join(ans)

        # data = s.split("]")
        #  [ 2, abc]3, cd]ef   ]
        #  [ 2[abc, 3[cd, ef      ]
        # ans = []
        # self.dd(data, ans, 0, 1)
        

    def dd(self, p, data):
        if p > len(data):
            return
        ans = []
        while p < len(data):
            letter = data[p]
            if letter.islower():
                ans.append(letter)
                p += 1
            elif letter.isnumeric():
                n_p = p
                num = []
                while data[n_p].isnumeric():
                    num.append(data[n_p])
                coef = int(''.join(num))
                ans += (coef *self.dd(n_p+1, data))
                p = n_p+1
            elif letter == "]":
                break
        
        return ans


                
            

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        final = []
        for i in range(len(s)):
            l = s[i]
            if len(final) == 0:
                final.append(l)
                continue
            if l in final:
                continue
            if final[-1] < l:
                final.append(l)
                continue
            if final[-1] > l:
                while(len(final) > 0):
                    if (final[-1]) in s[i:] and (final[-1] > l):
                        final.pop()
                    else:
                        break
                final.append(l)
        return ''.join(final)

       # s = list(s)
       # counts = {}
       # for i in range(len(s)):
       #   letter = s[i]
       #   if letter not in counts:
       #     counts[letter] = (1, [i])
       #   else:
       #     counts[letter][0] += 1
       #     counts[letter][1].append(i)

       # for (l, c) in counts:
       #   count = c[0]
       #   positions = c[1]
       #   if count == 1: continue

       #   for i in range(len(positions)-1):
       #     position = positions[i]
       #     s[i+1] > s[i]: continue
       #     #else
       #     s.pop(i)

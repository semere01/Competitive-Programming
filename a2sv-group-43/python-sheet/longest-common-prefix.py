class Solution:
    def longestCommonPrefix(self, str: list[str]) -> str:

        longestPrefix = []
        pointer = 0
        done = False
        strings = []
        for s in str:
            strings.append(list(s))
        print(strings)

        while not done:
            if pointer >= len(strings[0]):
                break
            longestPrefix.append(strings[0][pointer])
            for string in strings[1:]:
                if string == "":
                    return ""
                if longestPrefix != string[:pointer+1] or pointer >= len(string):
                    longestPrefix.pop()
                    done = True
                    break
                # if :
                #     longestPrefix.pop()
                #     done = True
                #     break
            pointer += 1

        return ''.join(longestPrefix)

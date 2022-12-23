class Solution:
    def interpret(self, command: str) -> str:
        command = list(command)
        pointer = 0
        final = []

        while (pointer < len(command)):
            if command[pointer] == "G":
                final.append("G")
                pointer += 1
            elif command[pointer] == "(":
                if (command[pointer+1] == ")"):
                    final.append("o")
                    pointer += 2
                elif (command[pointer+1] == "a"):
                    final.append("al")
                    pointer += 4
        return ''.join(final)

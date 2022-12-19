n = input()
bank = {}
line = []
for i in range(int(n)):
    word = input()
    try:
        bank[word] += 1
    except:
        bank[word] = 1
        line.append(word)

print(len(line))
if (len(line) > 1):
    for i in range(len(line)-1):
        print(f"{bank[line[i]]} ", end="")
print(bank[line[-1]])

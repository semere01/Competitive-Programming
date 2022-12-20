k = int(input())
inp = (input().split(" "))
inp.pop()
data = list(map(int, inp))
data.sort()
found = False
i = 0

while ((not found) and (i < len(data)-k)):
    if (data[i] == data[i+k-1]):
        i += k
        continue
    else:
        if (data[i] != data[i+1]):
            print(data[i])
            found = True
            break
        else:
            i += (k-1)


if not found:
    print(data[-1])

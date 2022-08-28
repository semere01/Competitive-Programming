t = int(input())
for x in range(t):
    l = int(input())
    data = [int(d) for d in input().split(" ")]
    evenParity = data[0]%2
    oddParity = data[1]%2
    canBeFlipped = True
    for i in range(l):
        d = data[i]
        if i % 2 == 0:
            canBeFlipped = (d%2 == evenParity)
        else:
            canBeFlipped = (d%2 == oddParity)
        if not canBeFlipped:
            break
    if canBeFlipped:
        print("YES")
    else:
        print("NO")

            


